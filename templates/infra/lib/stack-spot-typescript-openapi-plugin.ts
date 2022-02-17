import * as cdk from '@aws-cdk/core';
import { StackSpotOpenApiServices } from '@stackspot/cdk-component-openapi-typescript';

export class StackSpotTypescriptOpenApiPlugin {
    constructor(scope: cdk.Construct) {
        new StackSpotOpenApiServices(scope, 'StackSpotOpenApiServices', {
            specPath: 'spec/{{spec_file_name}}.yaml',
            sourceDir: '../{{source_dir}}'
        });
    }
}
