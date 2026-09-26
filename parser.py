def parse_struct(self):
    self.consume("STRUCT", "Expected 'struct42'")

    name = self.consume(
        "IDENTIFIER",
        "Expected struct name"
    )

    self.consume(
        "LBRACE",
        "Expected '{'"
    )

    fields = []

    while not self.check("RBRACE"):
        field_type = self.parse_type()

        field_name = self.consume(
            "IDENTIFIER",
            "Expected field name"
        )

        self.consume(
            "SEMICOLON",
            "Expected ';'"
        )

        fields.append(
            (field_name.value, field_type)
        )

    self.consume(
        "RBRACE",
        "Expected '}'"
    )

    return StructDecl(
        name.value,
        fields
    )
