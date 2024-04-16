<script>
    import fastapi from "../lib/api"

    let content = ""

    function get_record_detail() {
        fetch(`http://127.0.0.1:8000/records/record_detail/${record_id}`).then((response) => {
            response.json().then((json) => {
                record_detail = json
            })
        })
    }

    function update_record(event) {
        event.preventDefault() // 이벤트가 발생하면 동작 -> 오류 방지
        let url = "/records/update_record"
        let params = {
            content: content
        }
        fastapi('post', url, params, 
            (json) => {
                content = ''
                tmp()
                get_record_detail()
            }
        )
    }
</script>

<!-- 기록 입력 창 -->
<form method="post">
    <textarea rows="15" cols='100' bind:value={content}></textarea>
    <input type="submit" value="기록등록" on:click="{update_record}">
</form>
