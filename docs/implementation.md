## Enabling JWT Security
- The construct supports JWT tokens for security and the security can be enabled defining the following [OpenAPI security scheme](https://swagger.io/specification/#security-scheme-object):
```yaml
components:
  securitySchemes:
    jwtAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

- You can enable JWT token validation for all operations defining a securty constraint at api root level or at operation level as shown below:

```yaml
# root level
security:
  - jwtAuth: []
paths:
  /auctions/{id}:
    parameters:
      - $ref: '#/components/parameters/AuctionId'
      - $ref: '#/components/parameters/Authorization'
    get:
      operationId: get-auction
      description: Get auction data by id
      # operation level
      security:
        - jwtAuth: []
      tags:
        - Auction services
      responses:
        '200':
          description: Auction returned successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Auction'
        '404':
          description: Auction not found
```

- Most IDM providers expose a JWKS_URI with their public keys to verify JWT token signatures. You need to configure the construct as shown below to inform JWKS_URI to be used to get the public keys:

```typescript
const api = new StackSpotOpenApiServices(this, 'StackSampleAPI', {
  specPath: 'spec/auction-api.yaml',
  jwksUri: 'https://some.idm.provider/auth/realms/some-realm/protocol/openid-connect/certs',
});
```

- If you are using an IDM that supports OpenID connect you can get JWKS_URI endpoint in [well-known endpoint](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig) of OpenID connect provider.

- When you enable JWT authorization your controllers will extend `JWTAuthorizationController` class and you can override the `authorizeResourceAccess` method to do some custom authorization logic. The JWT token payload can be accessed using `this.jwtTokenPayload` protected property. Controlles already generated before JWT authorization will not be overwrited an must be changed by the user.

- With JWT Authorization enabled an API Gateway Lambda authorizer will be configured to validate the token.

- Authorization logic is not made by this lambda only the authenticity and validity of token is verified. You need to implement your authorization logic using token claims in operations controllers or create a new base constroller class based on `JWTAuthorizationControler` to use as base class of your controllers and implement authorization logic on it.

## Properties Definition

It's possible to configure properties on the construct as shown below:

```typescript
export interface StackSpotOpenAPIServicesProps {
  readonly specPath: string;
  readonly sourceDir?: string;
  readonly enableValidation?: boolean;
  readonly enableTracing?: boolean;
  readonly jwksUri?: string;
  readonly endpointTypes?: apigateway.EndpointType;
}
export declare enum EndpointType {
  /**
   * For an edge-optimized API and its custom domain name.
   *
   * @stability stable
   */
  EDGE = 'EDGE',
  /**
   * For a regional API and its custom domain name.
   *
   * @stability stable
   */
  REGIONAL = 'REGIONAL',
  /**
   * For a private API and its custom domain name.
   *
   * @stability stable
   */
  PRIVATE = 'PRIVATE',
}
const serviceProps: StackSpotOpenAPIServicesProps = {
  specPath: 'spec/auction-api.yaml',
  sourceDir: 'app/src',
  enableValidation: true,
  enableTracing: true,
  jwksUri: 'https://some.idm.provider/auth/realms/some-realm/protocol/openid-connect/certs',
  endpointTypes: EndpointType.EDGE,
};
const api = new StackSpotOpenApiServices(this, 'StackSpotOpenApiServicesID', serviceProps);
```

> **specPath**: Defines the path to OpenAPI specification file.  
> **sourceDir**: Defines the path to the source code generated based on OpenAPI specification file. **Default**: 'src'  
> **enableValidation**: If true, enable validators config in OpenAPI specification  
> **enableTracing**: If true, enable Amazon X-Ray tracing for ApiGateway and Lambda Function  
> **jwksUri**: JWKS URI to verify JWT Token signatures  
> **endpointTypes**: Defines the ApiGateway endpoint type. **Default**: EndpointType.EDGE

## References
### CDK

- <https://docs.aws.amazon.com/cdk/latest/guide/home.html> - CDK Developer guide
- <https://docs.aws.amazon.com/cdk/api/latest/docs/aws-apigateway-readme.html> - CDK Amazon API Gateway Construct Library
- <https://aws.github.io/jsii/user-guides/lib-author/> - jsii library author guide
- <https://cdk-advanced.workshop.aws/> - CDK advanced workshop
- <https://docs.aws.amazon.com/cdk/latest/guide/videos.html> - CDK Videos

### API Gateway

- <https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html> - API Gateway developer guide
- <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-validation-set-up.html#api-gateway-request-validation-setup-importing-swagger> - How to setup API Gateway validation with OpenAPI extensions
- <https://stackoverflow.com/questions/47953570/get-detailed-error-messages-from-aws-api-gateway-request-validator> - How to get detailed body request validation messages in API Gateway

### OpenAPI

- <https://swagger.io/specification/> - OpenAPI 3.0 specification
- <https://stoplight.io/studio/> - StopLight Studio for visual specification editor and other cool features
