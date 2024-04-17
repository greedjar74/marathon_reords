<script>
    import { link } from 'svelte-spa-router';

    let record_list = [];

    function get_record_list() {
        fetch("http://127.0.0.1:8000/records")
        .then((response) => {
            response.json().then((json) => {
                record_list = json
            })
        })
    }

    get_record_list();
</script>

<h1>마라톤 기록</h1>
<h3>
    {#each record_list as record}
        <li><a use:link href="/record_detail/{record.id}">{record.marathon}</a></li><br>
    {/each}
    <a use:link href="/update_record" class="btn btn-primary">기록 등록하기</a>
</h3>