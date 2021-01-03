mod dictionary;

use dictionary::iciba;
use structopt::StructOpt;

#[derive(Debug, StructOpt)]
struct Opt {
    #[structopt(name = "word")]
    word: String,

    #[structopt(name = "dictionary")]
    dictionary: Option<String>,
}

fn main() {
    let opt = Opt::from_args();
    let dictionary = match opt.dictionary {
        None => "iciba",
        Some(ref dictionary) => dictionary,
    };

    match dictionary {
        "iciba" => iciba::search(opt.word),
        _ => eprintln!("Unknown dictionary {}", dictionary),
    }
}
