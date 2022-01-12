PS=$(find ./pkg | grep .go)
for P in $PS
do
  go fmt "$P"
done