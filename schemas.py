upload_schema = {
    # Name of the table where data will be uploaded
	"name": "table_1",

    # The actual data for the table.
	"data": [
		{
            # Name of the column
			"column_name": "",

            #Type of the column
			"@type": "",

            # Values to be inserted into the column. If the type is a list, use a comma-separated string.
			"values": []
		},
	]
}


create_schema = {
    # Name of the table to be created
	"name": "",
    "columns": [
        {
            # Name of the column
            "name": "",
            
            # Type of the column
            "@type": "",

            # Indicates if the column is a primary key. If yes, set it to "true", otherwise leave it False.
            "is_primary_key": ""
        }
    ]
}