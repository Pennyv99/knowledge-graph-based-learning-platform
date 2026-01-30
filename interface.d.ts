interface Node {
    id: String,
    level: Number,
    message: String,
    Children: Array<Record<string, Node>>,
}

interface relationship {
    start: Number,
    end: Number,
    name: String,
}