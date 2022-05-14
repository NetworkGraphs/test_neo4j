CALL gds.fastRP.mutate('purchases',
  {
    embeddingDimension: 4,
    randomSeed: 42,
    mutateProperty: 'embedding',
    relationshipWeightProperty: 'amount',
    iterationWeights: [0.8, 1, 1, 1]
  }
)
YIELD nodePropertiesWritten
