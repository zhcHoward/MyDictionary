pub mod iciba;
use std::fmt;

pub trait Dictionary {
    fn search(&mut self);
    fn parse(&mut self);
    fn display(&self);
}

#[derive(Debug)]
struct Explaination {
    prop: String,
    explaination: Vec<String>,
}

impl Explaination {
    fn new(prop: String, explaination: Vec<String>) -> Self {
        Self { prop, explaination }
    }

    fn to_string(&self, offest: usize) -> String {
        format!(
            "{1:>0$} {2}",
            offest,
            &self.prop,
            &self.explaination.join("; ")
        )
    }
}

#[derive(Debug)]
struct Pronunciation {
    location: String,
    symbol: String,
}

impl Pronunciation {
    fn new(location: String, symbol: String) -> Self {
        Self { location, symbol }
    }

    fn to_string(&self) -> String {
        format!("{}[{}]", self.location, self.symbol)
    }
}

impl fmt::Display for Pronunciation {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}[{}]", self.location, self.symbol)
    }
}
