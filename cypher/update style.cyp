:style
node {
  diameter: 50px;
  color: #A5ABB6;
  border-color: #9AA1AC;
  border-width: 2px;
  text-color-internal: #FFFFFF;
  font-size: 10px;
}
relationship {
  color: #A5ABB6;
  shaft-width: 1px;
  font-size: 8px;
  padding: 3px;
  text-color-external: #000000;
  text-color-internal: #FFFFFF;
  caption: "<type>";
}
node.Database {
  color: #C990C0;
  border-color: #b261a5;
  text-color-internal: #FFFFFF;
  defaultCaption: "<id>";
  caption: "{name}";
}
node.Message {
  color: #F79767;
  border-color: #f36924;
  text-color-internal: #FFFFFF;
  defaultCaption: "<id>";
  caption: "{name}";
}
node.Person {
  color: #57C7E3;
  border-color: #23b3d7;
  text-color-internal: #2A2C34;
  caption: "{name}";
}
node.Product {
  color: #F16667;
  border-color: #eb2728;
  text-color-internal: #FFFFFF;
  caption: "{name}";
}
relationship.BUYS {
  shaft-width: 3px;
  color: #8DCC93;
  border-color: #5db665;
  text-color-internal: #2A2C34;
}
relationship.CHILD_OF {
  color: #54b8ff;
  border-color: #d7a013;
  text-color-internal: #2A2C34;
  shaft-width: 3px;
}
