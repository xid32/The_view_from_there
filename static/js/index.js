var myChart = echarts.init(document.getElementById('main'));
option = {
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
    },
    legend: {
        orient: 'vertical',
        left: 10,
        data: ['jiemian, China', 'huanqiu, China', 'apnews, U.S.', 'washingtonpost, U.S.', 'nytimes, U.S.','globaltimes, U.S.', 'The Hindu, India', 'Dainik Bhaskar, India']
    },
    series: [
        {
            name: 'Source of visit',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: false,
            label: {
                show: false,
                position: 'center'
            },
            emphasis: {
                label: {
                    show: true,
                    fontSize: '30',
                    fontWeight: 'bold'
                }
            },
            labelLine: {
                show: false
            },
            data: [
                {value: 0.1, name: 'jiemian, China'},
                {value: 0.1, name: 'huanqiu, China'},
                {value: 0.05, name: 'apnews, U.S.'},
                {value: 0.05, name: 'washingtonpost, U.S.'},
                {value: 0.05, name: 'nytimes, U.S.'},
                {value: 0.05, name: 'globaltimes, U.S.'},
                {value: 0.1, name: 'Dainik Bhaskar, India'},
                {value: 0.1, name: 'The Hindu, India'},
            ]
        }
    ]
};


myChart.setOption(option);

let oLoading = document.querySelectorAll(".loading")[0];
let oContent = document.querySelectorAll(".content")[0];

setTimeout(() => {
    oLoading.style.display = 'none';
    oContent.style.display = 'block';
}, 300);