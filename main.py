from templateframework.metadata import Metadata
from templateframework.runner import run
from templateframework.template import Template
import subprocess


def execute_npm_install(infra_resource_path: str):
    subprocess.run(['npm', 'install'], cwd=infra_resource_path)
    subprocess.run(['npm', 'install', '@stackspot/cdk-component-openapi-typescript@^0.7.4'], cwd=infra_resource_path)
    subprocess.run(['npm', 'install', '@types/aws-lambda@^8.10.86'], cwd=infra_resource_path)


def create_source_app(infra_resource_path: str, source_dir_path: str):
    subprocess.run(['npm', 'run', 'build'], cwd=infra_resource_path)
    subprocess.run(['npm', 'run', 'local', 'synth'], cwd=infra_resource_path)
    subprocess.run(['npm', 'install', '@types/aws-lambda@^8.10.86'], cwd=source_dir_path)
    subprocess.run(['npm', 'run', 'build'], cwd=source_dir_path)


class InitOpenApiPlugin(Template):
    def post_hook(self, metadata: Metadata):
        source_dir_path = metadata.target_path.joinpath(metadata.inputs['source_dir'])
        infra_resource_path = metadata.target_path.joinpath('infra')
        execute_npm_install(infra_resource_path)
        create_source_app(infra_resource_path, source_dir_path)


if __name__ == '__main__':
    run(InitOpenApiPlugin())
