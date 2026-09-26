# MiniLang Grammar

## Program

program -> declaration*

## Declaration

declaration -> struct_decl
             | function_decl
             | variable_decl

## Struct

struct_decl -> STRUCT IDENTIFIER '{' field_decl* '}'

field_decl -> type IDENTIFIER ';'

## Function

function_decl -> FUNC IDENTIFIER '(' parameters? ')' block

## Parameter

parameters -> parameter (',' parameter)*

parameter -> type IDENTIFIER

## Type

type -> INT
      | FLOAT
      | BOOL
      | IDENTIFIER

## Block

block -> '{' statement* '}'

## Statement

statement -> variable_decl
           | assignment
           | if_statement
           | while_statement
           | return_statement
           | function_decl
           | expression_statement

## If

if_statement -> IF '(' expression ')' block
               ELSE block

## While

while_statement -> WHILE '(' expression ')' block

## Return

return_statement -> RETURN expression? ';'

## Expression

expression -> equality

equality -> comparison (('==' | '!=') comparison)*

comparison -> term (('<' | '>' | '<=' | '>=') term)*

term -> factor (('+' | '-') factor)*

factor -> unary (('*' | '/') unary)*

unary -> ('!' | '-') unary
       | primary

primary -> NUMBER
         | STRING
         | IDENTIFIER
         | '(' expression ')'
