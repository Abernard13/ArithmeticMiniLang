<program>   ::= <expr> <eof>

<expr>      ::= <term> { ("+" | "-") <term> }

<term>      ::= <power> { ("*" | "/" | "%") <power> }

<power>     ::= <unary> [ "^" <power> ]
              (* exponentiation is right-associative *)

<unary>     ::= [ "+" | "-" ] <unary>
              | <primary>

<primary>   ::= <number>
              | "(" <expr> ")"

<number>    ::= <int> [ "." <int> ]

<int>       ::= <digit> { <digit> }

<digit>     ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

<eof>       ::=  (* end of input marker *)
