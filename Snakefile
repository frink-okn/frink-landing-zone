import glob

all_kg_files = glob.glob("docs/registry/kgs/*.md")

rule compile_registry:
    input:
        files=all_kg_files,
        script="scripts/combine_registry.py"
    output:
        "docs/registry/kgs.yaml"
    conda:
        "site_build_env.yaml"
    shell:
        """python {input.script} {output} {input.files}"""

rule generate_registry_index:
    input:
        files=all_kg_files,
        script="scripts/generate_registry_index.py"
    output:
        "docs/registry/index.md"
    conda:
        "site_build_env.yaml"
    shell:
        """python {input.script} {output} {input.files}"""
