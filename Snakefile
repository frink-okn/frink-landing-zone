import glob

all_kg_files = glob.glob("docs/registry/kgs/*.md")

rule compile_registry:
    input:
        all_kg_files
    output:
        "docs/registry/kgs.yaml"
    conda:
        "site_build_env.yaml"
    shell:
        """python scripts/combine_registry.py {output} {input}"""
