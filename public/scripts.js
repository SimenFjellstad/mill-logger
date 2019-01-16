var iterationCount = 0;
$(function() {
	function renderChart() {
		iterationCount++;
		$.ajax({
			url: '/data',
			success: function(data) {
				Highcharts.chart('chart', {
					chart: {
						zoomType: 'x',
					},
					series: data,
					title: {
						text: 'Temperature',
					},
					xAxis: {
						type: 'datetime',
						title: {
							text: 'Time',
						},
					},
					yAxis: {
						type: 'linear',
						title: {
							text: 'Temperature',
						},
						tickInterval: 5,
						labels: {
							formatter: function() {
								return this.value + ' \u00B0C';
							},
						},
					},
				});
			},
		});
	}
	renderChart();
	setInterval(renderChart, 60 * 1000);
});
