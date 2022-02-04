from pathlib import Path
from typing import List
from templateframework.metadata import Metadata
from templateframework.runner import run
from templateframework.template import Template
import subprocess


def read_file(file_path: Path):
    with file_path.open() as file:
        return file.readlines()


def write_in_stackfile(
        stackfile_path: Path,
        final_stackfile_lines: List[str],
        source_dir_path: str,
        spec_file_name: str
):
    with stackfile_path.open('w') as dockerfile_to_write:
        for line in final_stackfile_lines:
            dockerfile_to_write.write(line)
            if line.startswith('import * as cdk'):
                dockerfile_to_write.write(
                    'import { StackSpotOpenApiServices } from \'@stackspot/cdk-component-openapi-typescript\';\n'
                )
            elif line.endswith('super(scope, id, props);\n'):
                dockerfile_to_write.write(
                    '\t\tnew StackSpotOpenApiServices(this, \'StackSpotOpenApiServices\', {\n' +
                    '\t\t\tspecPath: \'spec/' + spec_file_name + '.yaml\',\n' +
                    '\t\t\tsourceDir: \'' + source_dir_path + '\'\n' +
                    '\t\t});\n'
                )


def execute_npm_install(infra_resource_path: str, source_dir_path: str):
    subprocess.run(['npm', 'install'], cwd=infra_resource_path)
    subprocess.run(
        ['npm', 'install', '-S', '@types/aws-lambda@^8.10.86', '@stackspot/cdk-component-openapi-typescript@^0.7.4'],
        cwd=infra_resource_path
    )
    subprocess.run(['npm', 'run', 'build'], cwd=infra_resource_path)
    subprocess.run(['npm', 'run', 'local', 'synth'], cwd=infra_resource_path)
    subprocess.run(['npm', 'install', '-S', '@types/aws-lambda@^8.10.86'], cwd=source_dir_path)
    subprocess.run(['npm', 'run', 'build'], cwd=source_dir_path)


class InitOpenApiPlugin(Template):
    def post_hook(self, metadata: Metadata):
        resource_path = metadata.target_path.joinpath('infra/lib')
        stackfile_path = resource_path.joinpath('service-name-service-stack.ts')
        stackfile_lines = read_file(stackfile_path)

        spec_file_name = metadata.inputs['spec_file_name']
        source_dir_path_str = metadata.inputs['source_dir']
        infra_resource_path = metadata.target_path.joinpath('infra')
        source_dir_path = infra_resource_path.joinpath(source_dir_path_str)
        write_in_stackfile(stackfile_path, stackfile_lines, source_dir_path_str, spec_file_name)

        execute_npm_install(infra_resource_path, source_dir_path)


if __name__ == '__main__':
    run(InitOpenApiPlugin())
