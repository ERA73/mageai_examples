# SNF data types
"""SELECT 
  column_name,
  data_type
FROM 
  information_schema.columns
WHERE 
  table_schema = 'PUBLIC' AND table_name = 'CLINICS';"""

import pandas as pd
import numpy as np

class TableMapper:
  def __init__(self):
    self.SNF_TO_POSTGRES={
        "BOOLEAN": "BOOLEAN",
        "NUMBER": ["BIGINT", "DECIMAL"],
        "FLOAT": "DOUBLE PRECISION",
        "STRING": "VARCHAR",
        "TEXT": "TEXT",
        "DATE": "DATE",
        "TIME": "TIME",
        "TIMESTAMP": "TIMESTAMP",
        "VARIANT": "JSONB",
        "ARRAY": "ARRAY",
        "OBJECT": "JSONB"
    }

    self.POSTGRES_TO_SNF={
        "BOOLEAN": "BOOLEAN",
        "BIGINT": "NUMBER",
        "DECIMAL": "NUMBER",
        "DOUBLE PRECISION": "FLOAT",
        "VARCHAR": "STRING",
        "TEXT": "TEXT",
        "DATE": "DATE",
        "TIME": "TIME",
        "TIMESTAMP": "TIMESTAMP",
        "JSONB": "OBJECT"
    }

    self.postgres_to_pandas = {
      'integer': 'int',
      'bigint': 'int64',
      'smallint': 'int16',
      'numeric': 'float64',
      'real': 'float32',
      'double precision': 'float64',
      'character varying': 'str',
      'character': 'str',
      'text': 'str',
      'date': 'datetime64[ns]',
      'timestamp without time zone': 'datetime64[ns]',
      'timestamp with time zone': 'datetime64[ns, UTC]',
      'boolean': 'bool'
    }

    self.snowflake_to_pandas = {
      'NUMBER': 'float64',
      'FLOAT': 'float64',
      'VARCHAR': 'str',
      'CHAR': 'str',
      'TEXT': 'str',
      'DATE': 'datetime64[ns]',
      'TIME': 'datetime64[ns]',
      'TIMESTAMP': 'datetime64[ns]',
      'BOOLEAN': 'bool'
    }

  def get_table_types(self, conn, schema, table_name):
    query = f"""
      SELECT 
        column_name,
        data_type,
        COALESCE(character_maximum_length::text, '') AS character_maximum_length,
        COALESCE(numeric_precision::text, '') AS numeric_precision,
        COALESCE(numeric_scale::text, '') AS numeric_scale
      FROM 
        information_schema.columns
      WHERE 
        table_schema = '{schema}' AND table_name = '{table_name}';
      """
    data = conn.load(query).to_dict('r')
    result = {value['column_name']: {k: v for k, v in value.items() if k != 'column_name'} for value in data}
    return result

  def apply_types(self, data, types):

    def astype_column(column, col_type):
      return column.astype(col_type, errors='ignore')
    
    def integer_column(column, col_type):
      return pd.to_numeric(column, errors='ignore').astype('Int8')
    
    def date_column(column):
      return pd.to_datetime(column, errors='coerce').date()
    
    def timestamp_column(column):
      return pd.to_datetime(column, errors='coerce')
    
    def timestamp_column_nz(column):
      return pd.to_datetime(column, errors='coerce', utc= True)
    
    def time_column(column):
      return pd.to_datetime(column, errors='coerce').dt.time

    def convert_array_to_list(column):
      return column.apply(lambda x: list(x) if x is not None else None, errors='coerce')

    def convert_json_to_dataframe(column):
      return pd.json_normalize(column, errors='coerce')

    column_functions = {
      'integer': [integer_column, 'int'],
      'bigint': [integer_column, 'int64'],
      'smallint': [integer_column, 'int16'],
      'numeric': [astype_column, 'float64'],
      'real': [astype_column, 'float32'],
      'double precision': [astype_column, 'float64'],
      'character varying': [astype_column, 'str'],
      'character': [astype_column, 'str'],
      'text': [astype_column, 'str'],
      'date': date_column,
      'timestamp without time zone': timestamp_column,
      'timestamp with time zone': timestamp_column_nz,
      'boolean': [astype_column, 'bool']
    }
    
    for column_name in data.columns:
      column_type = types[column_name]
      related_operation = column_functions[column_type]
      if isinstance(related_operation, list):
        related_function = related_operation[0]
        related_type = related_operation[1]
        data[column_name] = related_function(data[column_name], related_type)
      else:
        data[column_name] = related_operation(data[column_name])

    return data
  
  def generate_create_table_postgres(self, table_name, column_dict):
    columns = [f"{col} {data_type}" for col, data_type in column_dict.items()]
    columns_str = ", ".join(columns)
    return f"CREATE TABLE {table_name} ({columns_str});"

  def generate_create_table_snowflake(self, table_name, column_dict):
    columns = [f"{col} {data_type}" for col, data_type in column_dict.items()]
    columns_str = ", ".join(columns)
    return f"CREATE TABLE {table_name} ({columns_str});"
