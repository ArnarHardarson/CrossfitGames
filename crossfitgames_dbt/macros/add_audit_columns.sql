{% macro add_audit_columns() %}
    now() as audit_timestamp
{% endmacro %}
