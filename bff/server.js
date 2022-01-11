const {buildSchema} = require("graphql");


const schema = buildSchema(`
    type Query {
        studio(id: Int!): Studio
        studios(): [Studio]
    },
    type Mutation {
        createStudio(input: CreateStudioInput!): CreateStudioPayload!
        updateStudio(input: UpdateStudioInput!): UpdateStudioPayload!
    }
    type Studio {
        studio_id: ID!
        studio_name: String!
        introduction: String
        precaution: String
        homepage_url: String
        contact: String!
        address: Address!
        rent_by_min_hours: Float!
        can_free_cancel: Boolean
        
    }
`);