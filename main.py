import requests

webhook_url = 'https://discord.com/api/webhooks/1258659215267074128/CDnn_dHGyl5uEbhq4GbWYltujSDACbC_MMRjkWxtdNvGRybXguHecvmHerWYg0ubumzD'  # 복사한 웹훅 URL을 여기에 붙여넣기

data = {
    "content": "오늘도 잔디를 채웠다!",  # 메시지 내용
    "username": "WebhookBot"        # 웹훅에 표시될 이름
}

response = requests.post(webhook_url, json=data)

if response.status_code == 204:
    print("메시지가 성공적으로 전송되었습니다.")
else:
    print(f"메시지 전송 실패: {response.status_code}")
