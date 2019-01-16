var express = require('express');
var app = express();

const fs = require('fs');
const readline = require('readline');

require('dotenv').config();

app.use((req, res, next) => {
	res.header('Access-Control-Allow-Credentials', true);
	res.header('Access-Control-Allow-Origin', req.headers.origin);
	next();
});

app.use(express.static('public'));

app.get('/', (req, res) => {
	res.send('Hello World ' + process.env.ENVIRONMENT);
});

app.get('/data', (req, res) => {
	const lineReader = readline.createInterface({
		input: fs.createReadStream('document.csv'),
	});

	const lines = [];

	lineReader.on('line', function(line) {
		lines.push(line.split(','));
	});
	lineReader.on('close', () => {
		const series = convertMatrixToSeries(lines);
		res.json(series);
	});
});

app.listen(3000);
console.log('App listening to port 3000');

const extractColumn = (matrix, index, name, type = 'spline') => {
	const pointsOfData = 500;
	var returnEvery = Math.floor(matrix.length / pointsOfData);
	var output = [];
	for (var i = 0; i < matrix.length; i++) {
		if (i % returnEvery !== 0) continue;
		var row = matrix[i];
		output.push({
			y: parseFloat(row[index], 10),
			x: parseInt(row[0]) * 1000,
		});
	}
	return {
		name,
		type,
		data: output,
	};
};

const convertMatrixToSeries = matrix => {
	var outside_temperature = extractColumn(matrix, 1, 'Outside');
	var soverom_measured = extractColumn(matrix, 3, 'Bedroom Measured');
	var soverom_target = extractColumn(matrix, 4, 'Bedroom Target');
	var stue_measured = extractColumn(matrix, 6, 'Living room Measured');
	var stue_target = extractColumn(matrix, 7, 'Living room Target');
	return [
		outside_temperature,
		soverom_measured,
		soverom_target,
		stue_measured,
		stue_target,
	];
};
