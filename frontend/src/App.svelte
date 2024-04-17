<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from './routes/Detail.svelte';
  import Update from './routes/Update.svelte';
  import List from './routes/List.svelte';

  const routes = {
    '/': Home, // '/'과 '/records'가 맵핑
    '/records': List,
    '/record_detail/:record_id': Detail,
    '/update_record': Update,
  }
</script>

<Router {routes}/>