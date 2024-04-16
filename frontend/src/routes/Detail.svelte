<!-- 디테일 화면 -->
<!-- 특정 객체의 자세한 내용을 출력한다. -->
<script>
    import { params } from "svelte-spa-router/Router";

    export let record_detail = {}
    let record_id = params.record_id
    let record_detail = {}
  
    function get_record_detail(){
        fetch("http://127.0.0.1:8000/record_detail").then((response) => {
        response.json().then((json) => {
          record_detail = json
        })
      })
    }

    get_record_detail()
</script>
   
<h1>{record_detail.marathon}</h1>
<div>
    {record_detail.date}<br><br>
    {record_detail.bibnum}<br><br>
    {record_detail.record}<br><br>
    {record_detail.dnf}<br><br>
</div>