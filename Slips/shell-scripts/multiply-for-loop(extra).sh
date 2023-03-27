# accept a number and print its multiplication table using for loop

echo "Enter a number: "
read num

echo "Enter a range for multiplication:"
read range
 
# for loop
for (( i=1; i<=$range; i++ ))
do
    echo "$num * $i = $((num * i))"
done
