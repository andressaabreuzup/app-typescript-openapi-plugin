import * as cdk from '@aws-cdk/core';
import { StackSpotOpenApiServices } from '@stackspot/cdk-component-openapi-typescript';

export class {{service_name|title|replace("-", "")}}ServiceStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    new StackSpotOpenApiServices(this, 'StackSpotOpenApiServices', {
      specPath: 'spec/{{spec_file_name}}.yaml',
      sourceDir: '../{{source_dir}}'
    });
  }
}
