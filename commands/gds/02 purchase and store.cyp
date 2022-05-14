CALL gds.graph.project(
  'purchases',
  ['Person','Product'],
  {
    BUYS: {
      orientation: 'UNDIRECTED',
      properties: 'amount'
    }
  }
)
