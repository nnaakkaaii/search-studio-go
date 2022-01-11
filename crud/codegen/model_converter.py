import os


if __name__ == '__main__':
    flag = False
    with open(os.path.join('crud', 'models.py'), 'r') as f:
        text = f.read()
        text = text \
            .replace(
                'created_at = models.DateTimeField()',
                'created_at = models.DateTimeField(auto_now_add=True)',
            ) \
            .replace(
                'updated_at = models.DateTimeField()',
                'updated_at = models.DateTimeField(auto_now=True)'
            )
        print(text)
