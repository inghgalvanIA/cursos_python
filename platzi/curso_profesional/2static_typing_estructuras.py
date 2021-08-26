from typing import Dict, List

positivies: List[int] = [1,2,3,4,5]

users: Dict[str,int] = {
    "Argentina":2,
    "Mexico":34,
    "Colombia":45,
}

countries: List[Dict[str,str]] = [
    {
        "name": "Argentina",
        "people": "450000",
    },
    
    {
        "name": "Mexico",
        "people": "490000",
    },

    {
        "name": "Colombia",
        "people": "7150000",
    },
]




print(positivies)
print(type(positivies))
print(users)
print(type(users))
print(countries)
print(type(countries))