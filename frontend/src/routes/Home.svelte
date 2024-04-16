<script>
    let record_list = []
    import { link } from 'svelte-spa-router'

    let endpoint = "records"; // Default endpoint

    function get_record_list() {
        fetch("http://127.0.0.1:8000/records").then((response) => {
            response.json().then((json) => {
                record_list = json
            })
        })
    }

    get_record_list()

    function switchEndpoint(newEndpoint) {
      endpoint = newEndpoint;
      get_record_list().then(data => {
        record_list = data;
      });
    }
</script>

<select bind:value={endpoint} on:change={() => switchEndpoint(endpoint)}>
    <option value="records">Records</option>
    <option value="upate_record">Update Record</option>
  </select>

<h1><a use:link href="/update_record">새로운 기록이 있다면 입력해주세요</a></h1>
<h3>
    {#each record_list as record}
        <li><a use:link href="/record_detail/{record.id}">{record.marathon}</a></li><br>
    {/each}
</h3>
