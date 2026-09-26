def check_struct(self, node):
    if self.symbol_table.lookup(node.name):
        self.error(
            f"Duplicate struct declaration '{node.name}'"
        )
        return

    fields = {}

    for field_name, field_type in node.fields:

        if field_name in fields:
            self.error(
                f"Duplicate field '{field_name}' "
                f"in struct '{node.name}'"
            )

        fields[field_name] = field_type

    self.symbol_table.define(
        Symbol(
            node.name,
            fields,
            "struct"
        )
    )
