# API Usage

Measurement:
```json
{
  "meta": <meta>,
  "sensor_values": [
    {
      "sensor": <sensor_name>,
      "value": <value>
    }
  ]
}
```

Example:
```json
{
  "meta": "pico_one",
  "sensor_values": [
    {
      "sensor": "temp",
      "value": 20.3
    },
    {
      "sensor": "humidity",
      "value": 46
    }
  ]
}
```
