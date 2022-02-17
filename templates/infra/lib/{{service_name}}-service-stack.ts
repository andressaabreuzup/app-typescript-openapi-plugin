import * as cdk from '@aws-cdk/core';
import { StackSpotTypescriptOpenApiPlugin } from './stack-spot-typescript-openapi-plugin';

export class {{service_name|title|replace("-", "")}}ServiceStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    new StackSpotTypescriptOpenApiPlugin(this);
  }
}
