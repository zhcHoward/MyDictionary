pub mod iciba;

pub trait Dictionary {
    fn search(&mut self);
    fn parse(&mut self);
    fn display(&self);
}

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
