<script>
    let record_list = [];
    import { link } from 'svelte-spa-router';

    let endpoint = "records"; // Default endpoint
    let content = '';

    function get_record_list() {
        fetch("http://127.0.0.1:8000/records")
        .then(response => response.json())
        .then(json => {
            record_list = json;
        })
        .catch(error => {
            console.error('Error fetching record list:', error);
        });
    }

    function update_record(event) {
        event.preventDefault();

        const dataToSend = JSON.stringify({ content }); // 데이터를 문자열로 직접 변환

        fetch('http://127.0.0.1:8000/records/update_record', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: dataToSend, // 직접 문자열로 변환한 데이터를 body에 전달
        })
        .then(response => response.json())
        .then(jsonResponse => {
            console.log(jsonResponse);
            content = ''
        })
        .catch(error => {
            console.error('Error updating record:', error);
    });
}

    get_record_list();

    function switchEndpoint(newEndpoint) {
        endpoint = newEndpoint;
        if (endpoint === 'records') {
            get_record_list();
        } else {
            // 기록 업데이트 페이지로 이동
            // 현재 빈 문자열(content)로 업데이트 함수를 호출하도록 설정
            update_record({ preventDefault: () => {} });
        }
    }
</script>

<select bind:value={endpoint} on:change={() => switchEndpoint(endpoint)}>
    <option value="records">Records</option>
    <option value="update_record">Update Record</option> <!-- 수정: 오타 수정 -->
</select>

{#if endpoint === 'records'}
    <h1>마라톤 기록</h1>
    <h3>
        {#each record_list as record}
            <li><a use:link href="/record_detail/{record.id}">{record.marathon}</a></li><br>
        {/each}
    </h3>

{:else}
    <!-- 기록 입력 창 -->
    <form on:submit|preventDefault="{update_record}">
        <textarea rows="15" cols='100' bind:value={content}></textarea>
        <input type="submit" value="기록등록">
    </form>
{/if}
