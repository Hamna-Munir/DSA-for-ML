# Loops and Conditionals Example

loss_values = [0.9, 0.6, 0.4, 0.2]

for epoch in range(len(loss_values)):
    loss = loss_values[epoch]

    if loss < 0.3:
        print(f"Epoch {epoch}: Model performance is good")
    else:
        print(f"Epoch {epoch}: Training in progress")

# Output:
# Epoch 0: Training in progress
# Epoch 1: Training in progress
# Epoch 2: Training in progress
# Epoch 3: Model performance is good
