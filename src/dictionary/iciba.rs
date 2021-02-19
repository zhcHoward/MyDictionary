use crate::dictionary::{Dictionary, Explaination, Pronunciation};
use md5;
use reqwest::blocking::Client;
use serde_json::Value;
// use soup::{pattern::Pattern, QueryBuilderExt, Soup};
use std::collections::HashMap;
// use std::rc::Rc;
use std::time::{SystemTime, UNIX_EPOCH};

const URL: &str = "https://dict.iciba.com/dictionary/word/query/web";
const CLIENT: &str = "0";
const KEY: &str = "1000006";
const SEED: &str = "7ece94d9f9c202b0d2ec557dg4r9bc";

pub fn search(word: String) {
    let mut iciba = Iciba::new(word);
    iciba.search();
    iciba.parse();
    iciba.display();
}

struct Iciba {
    word: String,
    data: Value,
    pronunciation: Vec<Pronunciation>,
    explaination: Vec<Explaination>,
}

impl Iciba {
    fn new(word: String) -> Self {
        Iciba {
            word,
            data: Value::Null,
            pronunciation: vec![],
            explaination: vec![],
        }
    }

    fn parse_pronunciation(&mut self) {
        let data = &self.data[0];
        if let Some(symbol) = data.get("ph_am") {
            self.pronunciation
                .push(Pronunciation::new("美".to_string(), symbol.to_string()));
        }

        if let Some(symbol) = data.get("ph_en") {
            self.pronunciation
                .push(Pronunciation::new("英".to_string(), symbol.to_string()));
        }
    }

    fn parse_explaination(&mut self) {
        let data = &self.data[0]["parts"];
        self.explaination = data
            .as_array()
            .expect("explaination not found!")
            .iter()
            .map(|part| {
                let prop = part["part"].to_string();
                let meaning = part["means"]
                    .as_array()
                    .expect("means not found!")
                    .iter()
                    .map(|mean| mean.to_string())
                    .collect();
                Explaination::new(prop, meaning)
            })
            .collect();
    }
}

impl Dictionary for Iciba {
    fn search(&mut self) {
        // generate query
        let timestamp = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_millis()
            .to_string();
        let plain = format!(
            "{}{}{}{}{}{}",
            &URL[22..], // get only "path" part, not the full url
            CLIENT,
            KEY,
            &timestamp,
            &self.word,
            SEED
        );
        let md5sum = format!("{:x}", md5::compute(&plain));
        let mut query = HashMap::new();
        query.insert("client", CLIENT);
        query.insert("key", KEY);
        query.insert("word", &self.word);
        query.insert("timestamp", &timestamp);
        query.insert("signature", &md5sum);

        let client = Client::new();
        let req = client.get(URL).query(&query);
        let body: Value = req.send().unwrap().json().unwrap();
        self.data = body["message"]["baesInfo"]["symbols"].to_owned();
    }

    fn parse(&mut self) {
        self.parse_explaination();
        self.parse_pronunciation();
    }

    fn display(&self) {
        let offest = self
            .explaination
            .iter()
            .map(|exp| exp.prop.len())
            .max()
            .unwrap();
        println!(
            "{}\n{}",
            self.word,
            self.pronunciation
                .iter()
                .map(|pron| pron.to_string())
                .collect::<Vec<String>>()
                .join(" ")
        );
        for explaination in &self.explaination {
            println!("{}", explaination.to_string(offest as usize));
        }
    }
}

#[test]
fn test_parse_data() {
    let mut iciba = Iciba::new("book".to_string());
    iciba.search();
    iciba.parse();
    iciba.display();
}
