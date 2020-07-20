var data = `[{
    "Meta Data": {
    "1. Symbol": "XXX",
    "2. Last Refreshed": "2020-07-17 19:25:00",
    "3. Interval": "5min"
    },
    "Time Series (5min)": {
        "2020-07-17 19:25:00": {
        "1. open": "125.4800",
        "2. high": "125.4800",
        "3. low": "125.4800",
        "4. close": "125.4800",
        "5. volume": "100"
        },
        "2020-07-17 19:05:00": {
            "1. open": "125.2400",
            "2. high": "125.2400",
            "3. low": "125.2400",
            "4. close": "125.2400",
            "5. volume": "200"
        },
        "2020-07-17 19:00:00": {
            "1. open": "125.4000",
            "2. high": "125.4000",
            "3. low": "125.2400",
            "4. close": "125.2400",
            "5. volume": "1048"
        },
        "2020-07-17 18:40:00": {
            "1. open": "125.3000",
            "2. high": "125.3000",
            "3. low": "125.3000",
            "4. close": "125.3000",
            "5. volume": "248"
        },
        "2020-07-17 18:35:00": {
            "1. open": "125.3500",
            "2. high": "125.3500",
            "3. low": "125.3000",
            "4. close": "125.3000",
            "5. volume": "399"
        }
    }
}]`;

var bodyParsed = JSON.parse(data);
let bodyArray = []

// Meta Data #2
let metaData = bodyParsed[0]["Meta Data"];
let num2 = metaData["2. Last Refreshed"];
bodyArray.push(num2);

// Time series.
let timeSeries = bodyParsed[0]["Time Series (5min)"][num2];
bodyArray.push(
    timeSeries["1. open"],
    timeSeries["2. high"],
    timeSeries["3. low"],
    timeSeries["4. close"],
    timeSeries["5. volume"]
);

console.log(bodyArray);
