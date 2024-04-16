<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
    import Detail from './routes/Detail.svelte';

  const routes = {
    '/': Home, // '/'과 '/records'가 맵핑
    '/record_detail/:record_id': Detail,
  }
</script>

<Router {routes}/>