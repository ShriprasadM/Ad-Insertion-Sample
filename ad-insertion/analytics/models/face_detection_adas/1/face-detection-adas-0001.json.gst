{
"json_schema_version": "1.0.0",
"input_preproc":[
{
"color_format":"BGR"
}
],
"output_postproc":[
{
  "labels":["background","face"],
  "converter":"DetectionOutput",
  "layer_name":"detection_out"
}
]
}
