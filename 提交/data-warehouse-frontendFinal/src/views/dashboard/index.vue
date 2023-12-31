<template>
<body class='typora-export os-windows'><div class='typora-export-content'>
<div id='write'  class=''><h1 id='数据仓库项目报告'><span>数据仓库项目报告</span></h1><div class='md-toc' mdtype='toc'><p class="md-toc-content" role="list"><span role="listitem" class="md-toc-item md-toc-h1" data-ref="n339"><a class="md-toc-inner" href="#数据仓库项目报告">数据仓库项目报告</a></span><span role="listitem" class="md-toc-item md-toc-h1" data-ref="n527"><a class="md-toc-inner" href="#1-数据存储及优化对比">1 数据存储及优化对比</a></span><span role="listitem" class="md-toc-item md-toc-h2" data-ref="n340"><a class="md-toc-inner" href="#11-关系型数据库">1.1 关系型数据库</a></span><span role="listitem" class="md-toc-item md-toc-h3" data-ref="n341"><a class="md-toc-inner" href="#111-适用查询范围">1.1.1 适用查询范围</a></span><span role="listitem" class="md-toc-item md-toc-h3" data-ref="n350"><a class="md-toc-inner" href="#112-存储优化工作">1.1.2 存储优化工作</a></span><span role="listitem" class="md-toc-item md-toc-h3" data-ref="n397"><a class="md-toc-inner" href="#113-优化前后对比">1.1.3 优化前后对比</a></span><span role="listitem" class="md-toc-item md-toc-h2" data-ref="n402"><a class="md-toc-inner" href="#12-分布式数据库">1.2 分布式数据库</a></span><span role="listitem" class="md-toc-item md-toc-h3" data-ref="n403"><a class="md-toc-inner" href="#121-适用查询范围">1.2.1 适用查询范围</a></span><span role="listitem" class="md-toc-item md-toc-h3" data-ref="n416"><a class="md-toc-inner" href="#122-存储优化工作">1.2.2 存储优化工作</a></span><span role="listitem" class="md-toc-item md-toc-h3" data-ref="n424"><a class="md-toc-inner" href="#123-优化前后对比">1.2.3 优化前后对比</a></span><span role="listitem" class="md-toc-item md-toc-h2" data-ref="n427"><a class="md-toc-inner" href="#13-图数据库">1.3 图数据库</a></span><span role="listitem" class="md-toc-item md-toc-h3" data-ref="n428"><a class="md-toc-inner" href="#131-适用查询范围">1.3.1 适用查询范围</a></span><span role="listitem" class="md-toc-item md-toc-h3" data-ref="n437"><a class="md-toc-inner" href="#132-存储优化工作">1.3.2 存储优化工作</a></span><span role="listitem" class="md-toc-item md-toc-h3" data-ref="n451"><a class="md-toc-inner" href="#133-优化前后对比">1.3.3 优化前后对比</a></span><span role="listitem" class="md-toc-item md-toc-h1" data-ref="n454"><a class="md-toc-inner" href="#2-数据质量保证">2 数据质量保证</a></span><span role="listitem" class="md-toc-item md-toc-h2" data-ref="n455"><a class="md-toc-inner" href="#21-保证数据质量方法">2.1 保证数据质量方法</a></span><span role="listitem" class="md-toc-item md-toc-h2" data-ref="n485"><a class="md-toc-inner" href="#22-数据质量影响因素">2.2 数据质量影响因素</a></span><span role="listitem" class="md-toc-item md-toc-h1" data-ref="n501"><a class="md-toc-inner" href="#3-数据血缘使用场景">3 数据血缘使用场景</a></span><span role="listitem" class="md-toc-item md-toc-h1" data-ref="n520"><a class="md-toc-inner" href="#4-日志记录">4 日志记录</a></span></p></div><h1 id='1-数据存储及优化对比'><span>1 数据存储及优化对比</span></h1><h2 id='11-关系型数据库'><span>1.1 关系型数据库</span></h2><h3 id='111-适用查询范围'><span>1.1.1 适用查询范围</span></h3><p><span>关系型数据库在处理需要高度结构化数据和支持复杂查询的场景时表现良好。适用于需要数据一致性、完整性和事务处理的应用。</span></p><ul><li><span>关系型数据库基于表格模型，数据存储在由多个表格组成的关系中，每个表格包含多行数据和多个列（即属性），每个属性只有一种数据类型。采用关系代数等数学概念和方法来处理数据，使用结构化查询语言(SQL)进行查询和操作，所以适用于存储和检索结构化数据，但是需要定义好表和字段并保证数据结构固定且不经常发生变化。在本项目中，由于需要进行存储优化，在数据库结构进行了一些调整，比如进行添加冗余字段等，导致需要对数据进行更新或重新录入，在一些数据库表的操作上遇到了相当多的问题。</span></li><li><span>关系型数据库擅长应对复杂的关系和连接，允许在不同表之间建立关系，以执行联接操作；易于对数据进行分组和计算；还支持嵌套查询，对于在查询中使用子查询来获取特定条件下的数据非常有用；同时支持索引，通过在表上创建索引，可以提高查询性能，尤其是对于大型数据集</span></li><li><span>关系型数据库提供事务支持用于保证ACID属性，强调数据的完整性和一致性，数据结构清晰、易于理解、容易维护，适用于需要复杂查询、事务处理和保障保证数据一致性的场景，广泛应用于企业信息管理、金融系统、人力资源管理、学术研究等领域。</span></li></ul><h3 id='112-存储优化工作'><span>1.1.2 存储优化工作</span></h3><p><span>在本项目中，我们对物理模型进行反规范化，并通过建立索引等操作对存储进行优化</span></p><ol><li><span>星型模型使用</span></li></ol><p><span>本项目采用星型模型结构，对数据存储有一定的冗余。首先建立一个movie表，然后将movie的属性都</span></p><ol><li><p><span>字段设置</span></p><ol><li><span>在review表中，time字段记录了该评论的时间戳，我们并没有采用</span><code>datetime</code><span>等和时间有关的数据类型来存储时间戳，而是采用了</span><code>bigint</code><span>类型的数据来存储。使用bigint类型存储时间戳可以确保跨不同数据库和编程语言的一致性；相对于 </span><code>datetime</code><span> 类型，</span><code>bigint</code><span> 类型通常需要较少的存储空间，这对于像review表这样的行数很多的表来说，可以节省相当的存储空间。在某些情况下，使用 </span><code>bigint</code><span> 类型进行日期和时间的比较可能比使用 </span><code>datetime</code><span> 类型更高效。这是因为整数的比较操作通常比日期时间类型的比较要快。</span></li><li><span>在movie表中，我们使用</span><code>float</code><span>类型的数据来存储movie_score等和评分相关的数据。</span><code>float</code><span> 类型的存储空间通常小于 </span><code>double</code><span> 类型，而电影评分并不需要较高的精度，因此使用 </span><code>float</code><span> 可以减少存储空间的消耗。</span></li><li><span>在release_date表中，我们使用varchar类型的数据来存储year, month, day, weekday等字段。这允许存储非标准日期格式或混合格式数据直接以字符串形式存储日期时间等字段，也可以避免不同应用程序间日期格式解析的兼容性问题。对于这些字段，我们也建立了索引，加速了查询。</span></li></ol></li><li><p><span>冗余存储</span></p><ol><li><span>在电影表中存储相关评论数，在查询最受欢迎的演员组合时，可以避免与电影评论表进行join操作，由于电影评论表数据量巨大，所以会节省大量的时间</span></li><li><span>将时间单独抽象成一张表，将时间戳存储为不同数据格式，便于查询时直接进行匹配而不用处理数据，节省查询时间</span></li><li><span>我们对于评论的情感进行了两次优化，第一次将评论的情感单独抽象为一张表，避免根据情感进行查询时与原来的评论表进行join操作，但是由于是百万数量级，直接在电影表中增加一个字段，表示该电影中对应</span></li></ol></li><li><p><span>建立索引</span></p></li></ol><p><span>除了主键和外键等数据库自动建立的索引外，对查询操作中需要用到的字段建立单独的单列索引和组合索引，便于快速进行查询操作</span></p><ul><li><span>演员表中为演员姓名建立单列索引</span></li><li><span>导演表中为导演姓名建立单列索引</span></li><li><span>风格表中为电影风格建立单列索引</span></li><li><span>时间表中为年份建立单列索引，为年和月建立组合索引，为年和季度建立组合索引，为工作日建立单列索引</span></li><li><span>版本表中为电影语言建立单列索引，为电影格式建立单列索引</span></li></ul><ol><li><p><span>建立视图</span></p><ol><li><span>建立演员和演员之间合作的视图，字段包括演员1的id、演员2的id以及合作的电影id</span></li><li><span>建立演员和导演之间合作的视图，字段包括演员id、导演id以及合作的电影id</span></li></ol></li></ol><h3 id='113-优化前后对比'><span>1.1.3 优化前后对比</span></h3><p><span>在对评论的情感得分进行优化时，我们第一次选择将评论的情感得分单独抽象为一张表，在使用关系型数据库进行查询时，统计对应</span><code>movie_id</code><span> 的所有评论情感得分中大于0.2（我们设定的正面情感阈值）的比例，由于评论数量是百万数量级，最后的查询耗时较长（选择所有标题包含Harry的电影查看其信息，共需要56.938s）：</span></p><p><img src="https://hxejzbhvl9r.feishu.cn/space/api/box/stream/download/asynccode/?code=MDdjNjI2MTVkMTdjYTZhYjA3MmRiOWZkY2UzNWE0YWZfUlBEWThKQlU4MDFRQlkzeGlRSFlKeHRVN1F2ZVpUcjlfVG9rZW46VkpRRmJGOHlhb25xWTR4SExWN2NQeGllbm9iXzE3MDM5NTM0NjI6MTcwMzk1NzA2Ml9WNA" alt="img" style="zoom: 50%;" /><img src="https://hxejzbhvl9r.feishu.cn/space/api/box/stream/download/asynccode/?code=Yzc5YzY3YWNmOWYzNjg3M2IyNDNkYmZmOGFlNWUzZDBfakx0Z0tYd2J2MFFXWW15MlN2ZHlFeXNCYzZnd0hRazVfVG9rZW46WlFiSGJ1RjJHb21QUWJ4VktWWmNYT09pbkFnXzE3MDM5NTM0NjI6MTcwMzk1NzA2Ml9WNA" alt="img" style="zoom: 70%;" /></p><p><span>经过我们的优化，使用冗余存储，直接在电影表中增加一个字段</span><code>review_sentiment_rate</code><span>，查询同样的电影信息，只需要19.546s即可。</span></p><p><img src="https://hxejzbhvl9r.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2U5YzdmODdiNTA4OTQ3YmYyZmUyODIzNDA5NWVhOGVfbWltVVAyVVo5RVBTamhJaVZ0TXh4dW5aTWRhTXozeW5fVG9rZW46SFhjV2J5cWtQb1JVbDh4VU1qUWNFVzdzbm5oXzE3MDM5NTM0NjI6MTcwMzk1NzA2Ml9WNA" referrerpolicy="no-referrer" alt="img"></p><h2 id='12-分布式数据库'><span>1.2 分布式数据库</span></h2><h3 id='121-适用查询范围'><span>1.2.1 适用查询范围</span></h3><p><span>分布式数据库擅长于处理大规模数据和高并发访问，适用于需要横向扩展和高可用性的场景，包括大型互联网应用、大数据处理、分布式日志存储等</span></p><ul><li><span>具有扩容需求。分布式数据库支持水平扩展，允许数据分布在多个节点上。查询可以同时在多个节点上执行，从而提高系统的吞吐量和性能。特别是当数据库分库后，数据通常位于不同的节点，使用关系型数据库可以高效进行数据查询。并且分布式数据库可以处理分布式事务，允许在多个节点上执行的操作保持一致性，确保数据的一致性和完整性。</span></li><li><span>考虑负载均衡。分布式数据库通过负载均衡来分配查询负载，确保每个节点都在其容量范围内运行，同时可以优化查询执行计划，以充分利用分布式环境中多个节点的计算资源</span></li><li><span>性能需求严格。分布式数据库需要支持在不同节点上创建和维护索引，这有助于减少数据的传输并提高查询效率。为了加速查询性能，分布式数据库需要支持在不同节点上创建和维护索引。这有助于减少数据的传输并提高查询效率。</span></li><li><span>容错要求较高。分布式数据库需要具备容错和高可用性的特性，确保在节点故障或网络问题的情况下系统能够继续运行。这通常涉及数据备份、故障转移等机制</span></li><li><span>具有扩容需求。分布式的数据存储在不同的物理设备中，需要增加数据时，可以通过添加设备来横向拓展，解决容量问题</span></li></ul><h3 id='122-存储优化工作'><span>1.2.2 存储优化工作</span></h3><ol><li><span>将关系型数据库中的视图存储为实际的表，这样不仅可以复用之前的代码，还可以节省演员和演员以及演员和导演之间的join操作，加快查询速度</span></li><li><span>建立与关系型数据库相同的数据库表，通过冗余字段避免join操作，并建立了相同的索引以提高查询效率</span></li><li><span>建立外部表用于管理存储在数据库外部的数据，数据库中只存储元数据，而将实际数据存储到文件系统中，这种方式允许直接在数据所在位置进行查询处理，减少了数据移动的需要，避免其数据移动成为查询瓶颈，从而提升查询效率。</span></li></ol><h3 id='123-优化前后对比'><span>1.2.3 优化前后对比</span></h3><p><span>若不将视图建立为实际的表，则在分布式数据库中会出现更多的join操作，拖慢了查询的速度，在将视图建立为实际表后，速度加快了约5秒，下图是加快后的结果，查询时间为12.523s.</span></p><p><img src="https://hxejzbhvl9r.feishu.cn/space/api/box/stream/download/asynccode/?code=Zjc4MjU3ODE1N2U2ZmJmMzAwYmRmY2MxNGU5N2RkMWZfVHdTVzVsdldKWGpFZlZJcW96SjJtUXp0Q3ZkRHIxc1pfVG9rZW46S0tYN2JGODZpb1NydzZ4MDdnMGN4MWxablBoXzE3MDM5NTM0NjI6MTcwMzk1NzA2Ml9WNA" alt="img" style="zoom:80%;" /></p><h2 id='13-图数据库'><span>1.3 图数据库</span></h2><h3 id='131-适用查询范围'><span>1.3.1 适用查询范围</span></h3><p><span>图数据库专注于处理图形结构数据，擅长处理节点和边缘之间的关系，提供灵活的设计模式和高效的关联查询，适用于复杂的关系型数据，善于处理大量的、复杂的、互联的、多变的网状数据。支持数据的实时增删查改，保证ACID事务性，同时提供可视化、高可用、备份恢复等功能。</span></p><ul><li><span>复杂关系查询。图数据库擅长处理复杂的关系，可以轻松查找节点之间的关系，例如查找节点的邻居或查找共同的连接点。在本项目中，对演员和导演之间的关系进行查询时，使用关系型数据库不仅查询语句逻辑较为复杂（特别是查询两个人以上的组合时），并且运行效率较低，而使用图数据库进行查询即可简单且高效的获得不同节点之间的关系。</span></li><li><span>路径发现。图数据库支持查询两个节点之间的最短路径或所有可能的路径，并且内置了各种图算法，可以用于分析图中的重要节点、发现社区结构，对于路由规划、网络分析和依赖关系分析非常有用。</span></li><li><span>递归查询。图数据库支持递归查询，可以轻松地查找节点到其自身的路径，适用于存储和查询具有复杂关系模式的数据，这些关系模式难以用传统的关系型数据库模型表示，这对于查找包含自我引用关系的数据非常有用。</span></li></ul><h3 id='132-存储优化工作'><span>1.3.2 存储优化工作</span></h3><ol><li><p><span>存储字段选择</span></p><ol><li><span>在数据库中只存储三类节点(演员、导演、电影)以及两种关系(导演与电影间的执导关系和演员与电影之间的参演关系)，便于查询时快速进行计算</span></li><li><span>在数据库中电影节点中存储电影相关的评论数，便于统计</span></li></ol></li><li><p><span>建立索引</span></p><ol><li><span>对查询时三类节点中将会用到的字段建立索引，分别是演员名、演员名、电影名、电影风格</span></li></ol></li></ol><h3 id='133-优化前后对比'><span>1.3.3 优化前后对比</span></h3><p><span>建立图数据库索引可以加速图数据库关系的查询，左图是添加索引之前，查询演员之间的关系耗时为4.776秒，右图是添加索引之后，查询演员之间的关系耗时2.335秒。</span></p><p><img src="https://hxejzbhvl9r.feishu.cn/space/api/box/stream/download/asynccode/?code=MWIyNjg4MTZjMjRmNjgyMjA3NDZmMmY3YjUyNmFjM2RfZzhIV3R1Y0RWbWNHb2tLemlCOTdRZ0ZCRFBFSzRPaldfVG9rZW46SGRzNGJpVEpqb3ZwcFd4d3p0VmNBM0pnblRiXzE3MDM5NTM0NjI6MTcwMzk1NzA2Ml9WNA" alt="img" style="zoom: 67%;" /><img src="https://hxejzbhvl9r.feishu.cn/space/api/box/stream/download/asynccode/?code=NGIwOTE4NDUxOWM5NzdiN2QxYzBhMzYzMjg1MDJlM2VfMDl1cFRxZWM0ekxHVlNHOWJLYUVXWmk2d1R6OXg3aFZfVG9rZW46UDVTUGJEREdUb1dJejd4T0prZ2NzSVN6bllkXzE3MDM5NTM0NjI6MTcwMzk1NzA2Ml9WNA" alt="img" style="zoom: 75%;" /></p><h1 id='2-数据质量保证'><span>2 数据质量保证</span></h1><h2 id='21-保证数据质量方法'><span>2.1 保证数据质量方法</span></h2><ol><li><p><span>数据爬取</span></p><ol><li><span>使用爬虫获取数据时，使用selenium模拟浏览器操作，并使用amazoncaptcha库处理弹出的验证码进行反爬操作，爬取一定数量后更换ip地址(尝试建立代理池但是网上爬取的免费代理质量较差，所以手动切换代理节点)，并尝试更换cookie。组员之间使用各自不同的方式爬取数据，相互补充，并保留一份完整的网页数据，避免信息遗漏。</span></li><li><span>爬取时只爬取movies&amp;TV的数据</span></li><li><span>对爬取到的404网页进行标记</span></li><li><span>从网页中抽取数据时采用xpath，并且避免由于网页结构变化导致抽取数据失效</span></li></ol></li><li><p><span>数据清洗</span></p><ol><li><span>将组员之间的数据按ANSI进行merge操作，整理一份完整数据，避免数据遗漏</span></li><li><span>去除明显错误数据，包括除了电影id以外皆为空的数据等。</span></li><li><span>去除人名中的错误字符(比如双引号)</span></li><li><span>去除数据中不是movie的数据。首先对电影评价集进行处理，保留包含关键词film/movie的电影，然后去除电影名称中包含season/episode的数据</span></li><li><span>使用评论数据集中最早的评论时间填充缺失的部分电影上映时间</span></li><li><span>使用模糊匹配统一人名的不同表示形式，比如同一个姓名的缩写与全名，大小写等，统一为全名，优先呈现大写形式</span></li><li><span>对电影进行去重(电影名和导演相同即认为是同一部电影)时，保留重复组中的第一项，并用将要被去除的重复数据填充第一项中的空白数据</span></li></ol></li></ol><h2 id='22-数据质量影响因素'><span>2.2 数据质量影响因素</span></h2><ol><li><span>由于网页结构不同或者关键信息命名不同导致爬取信息不完整或者错误</span></li><li><span>由于是从单一数据源爬取数据，该电影的相关信息本就是不完整的，然后我们并没有使用第三方数据源进行补充(尝试使用豆瓣和TMDB的接口，但是对请求数有限制，接口也没有完全符合要求的，如果重新爬取过于麻烦)，也会影响数据质量</span></li><li><span>由于数据库本身设计可能存在缺陷，导致数据录入时无法校验或者校验不准确，导致数据重复或者不完整</span></li><li><span>由于Amazon采取的反爬虫措施阻碍了爬虫正常工作，影响数据的完整性和准确性。我们已经解决了验证码，但是在爬取的过程中发现验证码解决后的网页，detail部分的数据会被隐藏，导致重新爬取了近10条数据。</span></li><li><span>由于网络连接不稳定或中断可能导致数据爬取中断或部分数据丢失</span></li><li><span>由于不同数据库有不同的数据模型和约束，所以需要进行转换和验证，在这个过程中也会可能影响数据质量</span></li><li><span>由于数据清洗、转换、装载过程中，逻辑混乱导致数据出现丢失、重复、失真等质量问题。本项目由于进行了一次较大的数据库更新，重新处理了数据，过程中还涉及团队的相互合作，难以避免地出现一些对于数据的处理偏差，可能导致数据丢失或者重复</span></li></ol><h1 id='3-数据血缘使用场景'><span>3 数据血缘使用场景</span></h1><p><span>数据血缘是一种记录和追踪数据流动路径的技术，用于了解数据在整个信息系统中的传递、转换和处理过程。</span></p><ol><li><span>数据质量管理： 数据血缘可以用于监测和评估数据的质量。通过追踪数据流，可以识别数据质量问题的根本原因，快速定位数据质量问题的发生地点，以便进行及时修复和改进。</span></li><li><span>合规性和审计： 在需要遵循法规和标准的行业，数据血缘可以用于跟踪敏感数据的处理路径，确保数据的合规性。此外，审计人员可以使用数据血缘信息验证数据的准确性和完整性，以确保数据的可信度。</span></li><li><span>数据治理： 数据血缘是数据治理的关键组成部分。通过了解数据如何被创建、修改和使用，组织可以更好地管理其数据资产。数据血缘信息有助于制定数据治理政策、标准和规程，并确保其执行。</span></li><li><span>故障排查和性能优化： 在数据处理管道中发生故障或性能下降时，数据血缘可以帮助诊断问题。通过查看数据流的路径，可以迅速确定导致故障或性能问题的环节，并进行有效的排查和优化。</span></li><li><span>变更管理： 当数据架构或处理逻辑发生变更时，数据血缘可以追踪这些变更的影响。这有助于团队了解变更对数据流程的影响，减少潜在的风险和错误。</span></li><li><span>数据资产管理： 组织通常拥有大量的数据资产，包括数据集、报表和分析模型等。数据血缘可以用于跟踪这些数据资产的使用情况，了解哪些资产是关键的，哪些是过时的，以便进行有效的管理和优化。</span></li><li><span>数据安全： 在安全方面，数据血缘可以追踪敏感数据的流动路径，帮助组织了解数据的暴露风险。通过监控数据流动，可以及时发现潜在的安全漏洞和威胁。</span></li><li><span>业务影响分析： 当发生数据变更或系统升级时，了解数据血缘可以帮助业务部门了解这些变更对业务流程的影响。这对于规划和实施变更管理非常重要。</span></li></ol><h1 id='4-日志记录'><span>4 日志记录</span></h1><p><span>记录日志是计算机系统中的关键实践，主要用于故障排查、性能监测和安全审计。通过捕获关键事件和异常情况，日志有助于追踪问题、提高系统性能，并支持安全审计和合规性需求。此外，日志也在业务分析、版本跟踪和用户支持等方面发挥作用，为系统维护和优化提供重要信息。</span></p><p><span>本项目中，我们将对于三个数据库的操作以日志的形式记录到三个不同的日志文件中，便于进行问题定位等操作。3个日志文件及部分日志内容如下：</span></p><p><img src="https://hxejzbhvl9r.feishu.cn/space/api/box/stream/download/asynccode/?code=MzBkMjI1MjU0ODljOTNkZWNmZDViNmQ5ZjRhY2RmODNfNVRFNkp0ODVPRDd5MzZMbDFTbXAxbnprM21TektXWEhfVG9rZW46REdLcGJxZXZDb0tuYXR4VjRuMmNrdjF5bk1iXzE3MDM5NTM0NjI6MTcwMzk1NzA2Ml9WNA" referrerpolicy="no-referrer" alt="img"></p><p><img src="https://hxejzbhvl9r.feishu.cn/space/api/box/stream/download/asynccode/?code=MjY3OWYzYThkNTA5YmVkMjM1MzgwYWJmYTk5OWU2YWVfU0NoSlB1ZUpiM09CY1hyQ3FxaGh6NG14TWt0Z1JFYldfVG9rZW46QjladWJxVWFob0didlZ4dzliV2NCSmdkbmtoXzE3MDM5NTM0NjI6MTcwMzk1NzA2Ml9WNA" referrerpolicy="no-referrer" alt="img"></p></div></div>
</body>
</template>

<script>
export default {
  name: "Dashboard",
};
</script>

<style scoped>
.mac-os-11 { --title-bar-height:28px; }
html { font-size: 14px; background-color: var(--bg-color); color: var(--text-color); font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased; }
body { margin: 0px; padding: 0px; height: auto; inset: 0px; font-size: 1rem; line-height: 1.42857; overflow-x: hidden; background: inherit; tab-size: 4; }
iframe { margin: auto; }
a.url { word-break: break-all; }
a:active, a:hover { outline: 0px; }
.in-text-selection, ::selection { text-shadow: none; background: var(--select-text-bg-color); color: var(--select-text-font-color); }
#write { margin: 0px auto; height: auto; width: inherit; word-break: normal; overflow-wrap: break-word; position: relative; white-space: normal; overflow-x: visible; padding-top: 36px; }
#write.first-line-indent p { text-indent: 2em; }
#write.first-line-indent li p, #write.first-line-indent p * { text-indent: 0px; }
#write.first-line-indent li { margin-left: 2em; }
.for-image #write { padding-left: 8px; padding-right: 8px; }
body.typora-export { padding-left: 30px; padding-right: 30px; }
.typora-export .footnote-line, .typora-export li, .typora-export p { white-space: pre-wrap; }
.typora-export .task-list-item input { pointer-events: none; }
@media screen and (max-width: 500px) {
  body.typora-export { padding-left: 0px; padding-right: 0px; }
  #write { padding-left: 20px; padding-right: 20px; }
}
#write li > figure:last-child { margin-bottom: 0.5rem; }
#write ol, #write ul { position: relative; }
img { max-width: 100%; vertical-align: middle; image-orientation: from-image; }
button, input, select, textarea { color: inherit; font: inherit; }
input[type="checkbox"], input[type="radio"] { line-height: normal; padding: 0px; }
*, ::after, ::before { box-sizing: border-box; }
#write h1, #write h2, #write h3, #write h4, #write h5, #write h6, #write p, #write pre { width: inherit; }
#write h1, #write h2, #write h3, #write h4, #write h5, #write h6, #write p { position: relative; }
p { line-height: inherit; }
h1, h2, h3, h4, h5, h6 { break-after: avoid-page; break-inside: avoid; orphans: 4; }
p { orphans: 4; }
h1 { font-size: 2rem; }
h2 { font-size: 1.8rem; }
h3 { font-size: 1.6rem; }
h4 { font-size: 1.4rem; }
h5 { font-size: 1.2rem; }
h6 { font-size: 1rem; }
.md-math-block, .md-rawblock, h1, h2, h3, h4, h5, h6, p { margin-top: 1rem; margin-bottom: 1rem; }
.hidden { display: none; }
.md-blockmeta { color: rgb(204, 204, 204); font-weight: 700; font-style: italic; }
a { cursor: pointer; }
sup.md-footnote { padding: 2px 4px; background-color: rgba(238, 238, 238, 0.7); color: rgb(85, 85, 85); border-radius: 4px; cursor: pointer; }
sup.md-footnote a, sup.md-footnote a:hover { color: inherit; text-transform: inherit; text-decoration: inherit; }
#write input[type="checkbox"] { cursor: pointer; width: inherit; height: inherit; }
figure { overflow-x: auto; margin: 1.2em 0px; max-width: calc(100% + 16px); padding: 0px; }
figure > table { margin: 0px; }
thead, tr { break-inside: avoid; break-after: auto; }
thead { display: table-header-group; }
table { border-collapse: collapse; border-spacing: 0px; width: 100%; overflow: auto; break-inside: auto; text-align: left; }
table.md-table td { min-width: 32px; }
.CodeMirror-gutters { border-right: 0px; background-color: inherit; }
.CodeMirror-linenumber { user-select: none; }
.CodeMirror { text-align: left; }
.CodeMirror-placeholder { opacity: 0.3; }
.CodeMirror pre { padding: 0px 4px; }
.CodeMirror-lines { padding: 0px; }
div.hr:focus { cursor: none; }
#write pre { white-space: pre-wrap; }
#write.fences-no-line-wrapping pre { white-space: pre; }
#write pre.ty-contain-cm { white-space: normal; }
.CodeMirror-gutters { margin-right: 4px; }
.md-fences { font-size: 0.9rem; display: block; break-inside: avoid; text-align: left; overflow: visible; white-space: pre; background: inherit; position: relative !important; }
.md-fences-adv-panel { width: 100%; margin-top: 10px; text-align: center; padding-top: 0px; padding-bottom: 8px; overflow-x: auto; }
#write .md-fences.mock-cm { white-space: pre-wrap; }
.md-fences.md-fences-with-lineno { padding-left: 0px; }
#write.fences-no-line-wrapping .md-fences.mock-cm { white-space: pre; overflow-x: auto; }
.md-fences.mock-cm.md-fences-with-lineno { padding-left: 8px; }
.CodeMirror-line, twitterwidget { break-inside: avoid; }
svg { break-inside: avoid; }
.footnotes { opacity: 0.8; font-size: 0.9rem; margin-top: 1em; margin-bottom: 1em; }
.footnotes + .footnotes { margin-top: 0px; }
.md-reset { margin: 0px; padding: 0px; border: 0px; outline: 0px; vertical-align: top; background: 0px 0px; text-decoration: none; text-shadow: none; float: none; position: static; width: auto; height: auto; white-space: nowrap; cursor: inherit; -webkit-tap-highlight-color: transparent; line-height: normal; font-weight: 400; text-align: left; box-sizing: content-box; direction: ltr; }
li div { padding-top: 0px; }
blockquote { margin: 1rem 0px; }
li .mathjax-block, li p { margin: 0.5rem 0px; }
li blockquote { margin: 1rem 0px; }
li { margin: 0px; position: relative; }
blockquote > :last-child { margin-bottom: 0px; }
blockquote > :first-child, li > :first-child { margin-top: 0px; }
.footnotes-area { color: rgb(136, 136, 136); margin-top: 0.714rem; padding-bottom: 0.143rem; white-space: normal; }
#write .footnote-line { white-space: pre-wrap; }
@media print {
  body, html { border: 1px solid transparent; height: 99%; break-after: avoid; break-before: avoid; font-variant-ligatures: no-common-ligatures; }
  #write { margin-top: 0px; padding-top: 0px; border-color: transparent !important; padding-bottom: 0px !important; }
  .typora-export * { -webkit-print-color-adjust: exact; }
  .typora-export #write { break-after: avoid; }
  .typora-export #write::after { height: 0px; }
  .is-mac table { break-inside: avoid; }
  .typora-export-show-outline .typora-export-sidebar { display: none; }
}
.footnote-line { margin-top: 0.714em; font-size: 0.7em; }
a img, img a { cursor: pointer; }
pre.md-meta-block { font-size: 0.8rem; min-height: 0.8rem; white-space: pre-wrap; background: rgb(204, 204, 204); display: block; overflow-x: hidden; }
p > .md-image:only-child:not(.md-img-error) img, p > img:only-child { display: block; margin: auto; }
#write.first-line-indent p > .md-image:only-child:not(.md-img-error) img { left: -2em; position: relative; }
p > .md-image:only-child { display: inline-block; width: 100%; }
#write .MathJax_Display { margin: 0.8em 0px 0px; }
.md-math-block { width: 100%; }
.md-math-block:not(:empty)::after { display: none; }
.MathJax_ref { fill: currentcolor; }
[contenteditable="true"]:active, [contenteditable="true"]:focus, [contenteditable="false"]:active, [contenteditable="false"]:focus { outline: 0px; box-shadow: none; }
.md-task-list-item { position: relative; list-style-type: none; }
.task-list-item.md-task-list-item { padding-left: 0px; }
.md-task-list-item > input { position: absolute; top: 0px; left: 0px; margin-left: -1.2em; margin-top: calc(1em - 10px); border: none; }
.math { font-size: 1rem; }
.md-toc { min-height: 3.58rem; position: relative; font-size: 0.9rem; border-radius: 10px; }
.md-toc-content { position: relative; margin-left: 0px; }
.md-toc-content::after, .md-toc::after { display: none; }
.md-toc-item { display: block; color: rgb(65, 131, 196); }
.md-toc-item a { text-decoration: none; }
.md-toc-inner:hover { text-decoration: underline; }
.md-toc-inner { display: inline-block; cursor: pointer; }
.md-toc-h1 .md-toc-inner { margin-left: 0px; font-weight: 700; }
.md-toc-h2 .md-toc-inner { margin-left: 2em; }
.md-toc-h3 .md-toc-inner { margin-left: 4em; }
.md-toc-h4 .md-toc-inner { margin-left: 6em; }
.md-toc-h5 .md-toc-inner { margin-left: 8em; }
.md-toc-h6 .md-toc-inner { margin-left: 10em; }
@media screen and (max-width: 48em) {
  .md-toc-h3 .md-toc-inner { margin-left: 3.5em; }
  .md-toc-h4 .md-toc-inner { margin-left: 5em; }
  .md-toc-h5 .md-toc-inner { margin-left: 6.5em; }
  .md-toc-h6 .md-toc-inner { margin-left: 8em; }
}
a.md-toc-inner { font-size: inherit; font-style: inherit; font-weight: inherit; line-height: inherit; }
.footnote-line a:not(.reversefootnote) { color: inherit; }
.reversefootnote { font-family: ui-monospace, sans-serif; }
.md-attr { display: none; }
.md-fn-count::after { content: "."; }
code, pre, samp, tt { font-family: var(--monospace); }
kbd { margin: 0px 0.1em; padding: 0.1em 0.6em; font-size: 0.8em; color: rgb(36, 39, 41); background: rgb(255, 255, 255); border: 1px solid rgb(173, 179, 185); border-radius: 3px; box-shadow: rgba(12, 13, 14, 0.2) 0px 1px 0px, rgb(255, 255, 255) 0px 0px 0px 2px inset; white-space: nowrap; vertical-align: middle; }
.md-comment { color: rgb(162, 127, 3); opacity: 0.6; font-family: var(--monospace); }
code { text-align: left; vertical-align: initial; }
a.md-print-anchor { white-space: pre !important; border-width: initial !important; border-style: none !important; border-color: initial !important; display: inline-block !important; position: absolute !important; width: 1px !important; right: 0px !important; outline: 0px !important; background: 0px 0px !important; text-decoration: initial !important; text-shadow: initial !important; }
.os-windows.monocolor-emoji .md-emoji { font-family: "Segoe UI Symbol", sans-serif; }
.md-diagram-panel > svg { max-width: 100%; }
[lang="flow"] svg, [lang="mermaid"] svg { max-width: 100%; height: auto; }
[lang="mermaid"] .node text { font-size: 1rem; }
table tr th { border-bottom: 0px; }
video { max-width: 100%; display: block; margin: 0px auto; }
iframe { max-width: 100%; width: 100%; border: none; }
.highlight td, .highlight tr { border: 0px; }
mark { background: rgb(255, 255, 0); color: rgb(0, 0, 0); }
.md-html-inline .md-plain, .md-html-inline strong, mark .md-inline-math, mark strong { color: inherit; }
.md-expand mark .md-meta { opacity: 0.3 !important; }
mark .md-meta { color: rgb(0, 0, 0); }
@media print {
  .typora-export h1, .typora-export h2, .typora-export h3, .typora-export h4, .typora-export h5, .typora-export h6 { break-inside: avoid; }
}
.md-diagram-panel .messageText { stroke: none !important; }
.md-diagram-panel .start-state { fill: var(--node-fill); }
.md-diagram-panel .edgeLabel rect { opacity: 1 !important; }
.md-fences.md-fences-math { font-size: 1em; }
.md-fences-advanced:not(.md-focus) { padding: 0px; white-space: nowrap; border: 0px; }
.md-fences-advanced:not(.md-focus) { background: inherit; }
.typora-export-show-outline .typora-export-content { max-width: 1440px; margin: auto; display: flex; flex-direction: row; }
.typora-export-sidebar { width: 300px; font-size: 0.8rem; margin-top: 80px; margin-right: 18px; }
.typora-export-show-outline #write { --webkit-flex:2; flex: 2 1 0%; }
.typora-export-sidebar .outline-content { position: fixed; top: 0px; max-height: 100%; overflow: hidden auto; padding-bottom: 30px; padding-top: 60px; width: 300px; }
@media screen and (max-width: 1024px) {
  .typora-export-sidebar, .typora-export-sidebar .outline-content { width: 240px; }
}
@media screen and (max-width: 800px) {
  .typora-export-sidebar { display: none; }
}
.outline-content li, .outline-content ul { margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; list-style: none; }
.outline-content ul { margin-top: 0px; margin-bottom: 0px; }
.outline-content strong { font-weight: 400; }
.outline-expander { width: 1rem; height: 1.42857rem; position: relative; display: table-cell; vertical-align: middle; cursor: pointer; padding-left: 4px; }
.outline-expander::before { content: ""; position: relative; font-family: Ionicons; display: inline-block; font-size: 8px; vertical-align: middle; }
.outline-item { padding-top: 3px; padding-bottom: 3px; cursor: pointer; }
.outline-expander:hover::before { content: ""; }
.outline-h1 > .outline-item { padding-left: 0px; }
.outline-h2 > .outline-item { padding-left: 1em; }
.outline-h3 > .outline-item { padding-left: 2em; }
.outline-h4 > .outline-item { padding-left: 3em; }
.outline-h5 > .outline-item { padding-left: 4em; }
.outline-h6 > .outline-item { padding-left: 5em; }
.outline-label { cursor: pointer; display: table-cell; vertical-align: middle; text-decoration: none; color: inherit; }
.outline-label:hover { text-decoration: underline; }
.outline-item:hover { border-color: rgb(245, 245, 245); background-color: var(--item-hover-bg-color); }
.outline-item:hover { margin-left: -28px; margin-right: -28px; border-left: 28px solid transparent; border-right: 28px solid transparent; }
.outline-item-single .outline-expander::before, .outline-item-single .outline-expander:hover::before { display: none; }
.outline-item-open > .outline-item > .outline-expander::before { content: ""; }
.outline-children { display: none; }
.info-panel-tab-wrapper { display: none; }
.outline-item-open > .outline-children { display: block; }
.typora-export .outline-item { padding-top: 1px; padding-bottom: 1px; }
.typora-export .outline-item:hover { margin-right: -8px; border-right: 8px solid transparent; }
.typora-export .outline-expander::before { content: "+"; font-family: inherit; top: -1px; }
.typora-export .outline-expander:hover::before, .typora-export .outline-item-open > .outline-item > .outline-expander::before { content: "−"; }
.typora-export-collapse-outline .outline-children { display: none; }
.typora-export-collapse-outline .outline-item-open > .outline-children, .typora-export-no-collapse-outline .outline-children { display: block; }
.typora-export-no-collapse-outline .outline-expander::before { content: "" !important; }
.typora-export-show-outline .outline-item-active > .outline-item .outline-label { font-weight: 700; }
.md-inline-math-container mjx-container { zoom: 0.95; }
mjx-container { break-inside: avoid; }


:root {
    --side-bar-bg-color: #fafafa;
    --control-text-color: #777;
}

@include-when-export url(https://fonts.loli.net/css?family=Open+Sans:400italic,700italic,700,400&subset=latin,latin-ext);

/* open-sans-regular - latin-ext_latin */
  /* open-sans-italic - latin-ext_latin */
    /* open-sans-700 - latin-ext_latin */
    /* open-sans-700italic - latin-ext_latin */
  html {
    font-size: 16px;
    -webkit-font-smoothing: antialiased;
}

body {
    font-family: "Open Sans","Clear Sans", "Helvetica Neue", Helvetica, Arial, 'Segoe UI Emoji', sans-serif;
    color: rgb(51, 51, 51);
    line-height: 1.6;
}

#write {
    max-width: 860px;
  	margin: 0 auto;
  	padding: 30px;
    padding-bottom: 100px;
}

@media only screen and (min-width: 1400px) {
	#write {
		max-width: 1024px;
	}
}

@media only screen and (min-width: 1800px) {
	#write {
		max-width: 1200px;
	}
}

#write > ul:first-child,
#write > ol:first-child{
    margin-top: 30px;
}

a {
    color: #4183C4;
}
h1,
h2,
h3,
h4,
h5,
h6 {
    position: relative;
    margin-top: 1rem;
    margin-bottom: 1rem;
    font-weight: bold;
    line-height: 1.4;
    cursor: text;
}
h1:hover a.anchor,
h2:hover a.anchor,
h3:hover a.anchor,
h4:hover a.anchor,
h5:hover a.anchor,
h6:hover a.anchor {
    text-decoration: none;
}
h1 tt,
h1 code {
    font-size: inherit;
}
h2 tt,
h2 code {
    font-size: inherit;
}
h3 tt,
h3 code {
    font-size: inherit;
}
h4 tt,
h4 code {
    font-size: inherit;
}
h5 tt,
h5 code {
    font-size: inherit;
}
h6 tt,
h6 code {
    font-size: inherit;
}
h1 {
    font-size: 2.25em;
    line-height: 1.2;
    border-bottom: 1px solid #eee;
}
h2 {
    font-size: 1.75em;
    line-height: 1.225;
    border-bottom: 1px solid #eee;
}

/*@media print {
    .typora-export h1,
    .typora-export h2 {
        border-bottom: none;
        padding-bottom: initial;
    }

    .typora-export h1::after,
    .typora-export h2::after {
        content: "";
        display: block;
        height: 100px;
        margin-top: -96px;
        border-top: 1px solid #eee;
    }
}*/

h3 {
    font-size: 1.5em;
    line-height: 1.43;
}
h4 {
    font-size: 1.25em;
}
h5 {
    font-size: 1em;
}
h6 {
   font-size: 1em;
    color: #777;
}
p,
blockquote,
ul,
ol,
dl,
table{
    margin: 0.8em 0;
}
li>ol,
li>ul {
    margin: 0 0;
}
hr {
    height: 2px;
    padding: 0;
    margin: 16px 0;
    background-color: #e7e7e7;
    border: 0 none;
    overflow: hidden;
    box-sizing: content-box;
}

li p.first {
    display: inline-block;
}
ul,
ol {
    padding-left: 30px;
}
ul:first-child,
ol:first-child {
    margin-top: 0;
}
ul:last-child,
ol:last-child {
    margin-bottom: 0;
}
blockquote {
    border-left: 4px solid #dfe2e5;
    padding: 0 15px;
    color: #777777;
}
blockquote blockquote {
    padding-right: 0;
}
table {
    padding: 0;
    word-break: initial;
}
table tr {
    border: 1px solid #dfe2e5;
    margin: 0;
    padding: 0;
}
table tr:nth-child(2n),
thead {
    background-color: #f8f8f8;
}
table th {
    font-weight: bold;
    border: 1px solid #dfe2e5;
    border-bottom: 0;
    margin: 0;
    padding: 6px 13px;
}
table td {
    border: 1px solid #dfe2e5;
    margin: 0;
    padding: 6px 13px;
}
table th:first-child,
table td:first-child {
    margin-top: 0;
}
table th:last-child,
table td:last-child {
    margin-bottom: 0;
}

.CodeMirror-lines {
    padding-left: 4px;
}

.code-tooltip {
    box-shadow: 0 1px 1px 0 rgba(0,28,36,.3);
    border-top: 1px solid #eef2f2;
}

.md-fences,
code,
tt {
    border: 1px solid #e7eaed;
    background-color: #f8f8f8;
    border-radius: 3px;
    padding: 0;
    padding: 2px 4px 0px 4px;
    font-size: 0.9em;
}

code {
    background-color: #f3f4f4;
    padding: 0 2px 0 2px;
}

.md-fences {
    margin-bottom: 15px;
    margin-top: 15px;
    padding-top: 8px;
    padding-bottom: 6px;
}


.md-task-list-item > input {
  margin-left: -1.3em;
}

@media print {
    html {
        font-size: 13px;
    }
    pre {
        page-break-inside: avoid;
        word-wrap: break-word;
    }
}

.md-fences {
	background-color: #f8f8f8;
}
#write pre.md-meta-block {
	padding: 1rem;
    font-size: 85%;
    line-height: 1.45;
    background-color: #f7f7f7;
    border: 0;
    border-radius: 3px;
    color: #777777;
    margin-top: 0 !important;
}

.mathjax-block>.code-tooltip {
	bottom: .375rem;
}

.md-mathjax-midline {
    background: #fafafa;
}

#write>h3.md-focus:before{
	left: -1.5625rem;
	top: .375rem;
}
#write>h4.md-focus:before{
	left: -1.5625rem;
	top: .285714286rem;
}
#write>h5.md-focus:before{
	left: -1.5625rem;
	top: .285714286rem;
}
#write>h6.md-focus:before{
	left: -1.5625rem;
	top: .285714286rem;
}
.md-image>.md-meta {
    /*border: 1px solid #ddd;*/
    border-radius: 3px;
    padding: 2px 0px 0px 4px;
    font-size: 0.9em;
    color: inherit;
}

.md-tag {
    color: #a7a7a7;
    opacity: 1;
}

.md-toc { 
    margin-top:20px;
    padding-bottom:20px;
}

.sidebar-tabs {
    border-bottom: none;
}

#typora-quick-open {
    border: 1px solid #ddd;
    background-color: #f8f8f8;
}

#typora-quick-open-item {
    background-color: #FAFAFA;
    border-color: #FEFEFE #e5e5e5 #e5e5e5 #eee;
    border-style: solid;
    border-width: 1px;
}

/** focus mode */
.on-focus-mode blockquote {
    border-left-color: rgba(85, 85, 85, 0.12);
}

header, .context-menu, .megamenu-content, footer{
    font-family: "Segoe UI", "Arial", sans-serif;
}

.file-node-content:hover .file-node-icon,
.file-node-content:hover .file-node-open-state{
    visibility: visible;
}

.mac-seamless-mode #typora-sidebar {
    background-color: #fafafa;
    background-color: var(--side-bar-bg-color);
}

.md-lang {
    color: #b4654d;
}

/*.html-for-mac {
    --item-hover-bg-color: #E6F0FE;
}*/

#md-notification .btn {
    border: 0;
}

.dropdown-menu .divider {
    border-color: #e5e5e5;
    opacity: 0.4;
}

.ty-preferences .window-content {
    background-color: #fafafa;
}

.ty-preferences .nav-group-item.active {
    color: white;
    background: #999;
}

.menu-item-container a.menu-style-btn {
    background-color: #f5f8fa;
    background-image: linear-gradient( 180deg , hsla(0, 0%, 100%, 0.8), hsla(0, 0%, 100%, 0)); 
}

.CodeMirror-wrap .CodeMirror-code pre {	
	font-family: "JetBrains Mono", "Microsoft YaHei"
}
</style>
