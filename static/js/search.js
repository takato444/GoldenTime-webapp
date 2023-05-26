document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault(); // 阻止表单默认提交行为

    var keyword = document.getElementById('search-input').value;
    performSearch(keyword);
});

function performSearch(keyword) {
    // 在这里执行搜索操作
    // 根据关键字获取相关结果

    // 这里只是一个示例，您需要根据您的实际情况进行修改
    var results = [
        { title: '结果1', url: 'https://example.com/result1' },
        { title: '结果2', url: 'https://example.com/result2' },
        { title: '结果3', url: 'https://example.com/result3' }
    ];

    showResults(results);
}

function showResults(results) {
    var resultsContainer = document.getElementById('search-results');
    resultsContainer.innerHTML = ''; // 清空容器

    if (results.length === 0) {
        resultsContainer.innerText = '没有找到相关结果。';
        return;
    }

    // 创建结果列表
    var ul = document.createElement('ul');

    results.forEach(function(result) {
        // 创建列表项
        var li = document.createElement('li');

        // 创建链接
        var link = document.createElement('a');
        link.href = result.url;
        link.textContent = result.title;

        // 将链接添加到列表项
        li.appendChild(link);

        // 将列表项添加到列表
        ul.appendChild(li);
    });

    // 将列表添加到容器
    resultsContainer.appendChild(ul);
}
