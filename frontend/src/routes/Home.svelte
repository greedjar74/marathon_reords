<!-- 메인 화면 -->
<!-- 각 객체의 대회명을 리스트 형태로 출력한다. -->
<script>
    import { link } from 'svelte-spa-router' // link 속성을 위해 import
    let records_list = []
  
    function get_records() {
      fetch("http://127.0.0.1:8000/records").then((response) => {
        response.json().then((json) => {
          records_list = json
        })
      })
    }
  
    get_records()
  </script>
  
  <ul>
    {#each records_list as record}
      <li><a use:link href="/record_detail/{record.id}">{record.marathon}</a></li>
    {/each}
  </ul>
  