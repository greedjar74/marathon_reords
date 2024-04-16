<!-- App의 frontend에 대한 메인 코드 -->
<!-- 각 라우터를 불러와 특정 도메인의 화면을 보여준다. -->

<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"

  const routes = {
    '/': Home, // 'http://localhost:5173/'는 'http://127.0.0.1:8000/records'으로 매핑 되었다. 즉 /이 /records로 매핑된 것
    'detail/:record_id': Detail // 특정 기록에 대해서 자세한 내용을 출력하는 화면
  }
</script>

<Router {routes}/>
