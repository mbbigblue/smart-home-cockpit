from dataclasses import dataclass
import json


@dataclass
class MeasurementRecord:
    id: str
    name: str
    location: str
    timestamp: str
    puser: str
    active: bool
    value: float
    scale: str
    comment: str


record = MeasurementRecord(id="123f",
                           location="New York City",
                           timestamp="10-04-19 12:00:17",
                           puser="Jack Strong",
                           active=True,
                           name="Temperature",
                           value=17.3,
                           scale="C",
                           comment="Basement"
                           )


jsonStr = json.dumps(record.__dict__)

#print json string
print(jsonStr)