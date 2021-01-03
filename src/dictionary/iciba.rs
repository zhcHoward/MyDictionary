use crate::dictionary::{Dictionary, Explaination};
use reqwest::blocking::Client;
use soup::{pattern::Pattern, NodeExt, QueryBuilderExt, Soup};
use std::rc::Rc;

const URL: &str = "https://www.iciba.com/word";

pub fn search(word: String) {
    let mut iciba = Iciba::new(word);
    iciba.search();
    iciba.parse();
    iciba.display();
}

struct Iciba {
    word: String,
    html: String,
    pronunciation: Vec<String>,
    explaination: Vec<Explaination>,
}

impl Iciba {
    fn new(word: String) -> Self {
        Iciba {
            word,
            html: String::new(),
            pronunciation: vec![],
            explaination: vec![],
        }
    }

    fn parse_pronunciation<Q: QueryBuilderExt>(&mut self, block: Q) {
        let pblock = block
            .class(StartsWith::new("Mean_symbols_"))
            .find()
            .expect("Mean_symbols not found");
        self.pronunciation = pblock.children().map(|li| li.text()).collect();
    }

    fn parse_explaination<Q: QueryBuilderExt>(&mut self, block: Q) {
        let meaning = block
            .class(StartsWith::new("Mean_part_"))
            .find()
            .expect("Mean_part not found");
        self.explaination = meaning
            .children()
            .map(|node| {
                let prop = node.tag("i").find().expect("prop not found").text();
                let meanings = node
                    .tag("div")
                    .find()
                    .expect("div not found")
                    .children()
                    .map(|span| span.text().trim_end_matches("; ").to_string())
                    .collect();
                Explaination::new(prop, meanings)
            })
            .collect();
    }
}

impl Dictionary for Iciba {
    fn search(&mut self) {
        let client = Client::new();
        let req = client.get(URL).query(&[("w", &self.word)]);
        self.html = req.send().unwrap().text().unwrap();
    }

    fn parse(&mut self) {
        let soup = Soup::new(&self.html);
        let mean_block = soup
            .class(StartsWith::new("Mean_mean_"))
            .find()
            .expect("Mean_mean not found");
        self.parse_explaination(Rc::clone(&mean_block));
        self.parse_pronunciation(mean_block);
    }

    fn display(&self) {
        let offest = self
            .explaination
            .iter()
            .map(|exp| exp.prop.len())
            .max()
            .unwrap();
        println!("{}\n{}", self.word, self.pronunciation.join(" "));
        for explaination in &self.explaination {
            println!("{}", explaination.to_string(offest as usize));
        }
    }
}

struct StartsWith<'a> {
    prefix: &'a str,
}

impl<'a> StartsWith<'a> {
    fn new(prefix: &'a str) -> Self {
        Self { prefix }
    }
}

impl Pattern for StartsWith<'_> {
    fn matches(&self, haystack: &str) -> bool {
        haystack.starts_with(self.prefix)
    }
}

#[test]
fn test_parse_data() {
    let mut iciba = Iciba::new("book".to_string());
    iciba.search();
    iciba.parse();
    iciba.display();
}