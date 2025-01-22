from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
from .models import GameState

def landing(request):
    return render(request, 'life/landing.html')

def game(request):
    return render(request, 'life/game.html')

def select_pattern(request):
    return render(request, 'life/select_pattern.html')

def initialize_grid(width=50, height=50):
    return np.random.choice([0, 1], size=(height, width), p=[0.85, 0.15]).tolist()

def calculate_next_generation(grid):
    grid = np.array(grid)
    rows, cols = grid.shape
    next_gen = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            # Count live neighbors using periodic boundary conditions
            total = int((grid[i, (j-1)%cols] + grid[i, (j+1)%cols] + 
                        grid[(i-1)%rows, j] + grid[(i+1)%rows, j] + 
                        grid[(i-1)%rows, (j-1)%cols] + grid[(i-1)%rows, (j+1)%cols] + 
                        grid[(i+1)%rows, (j-1)%cols] + grid[(i+1)%rows, (j+1)%cols]))
            
            # Apply Conway's Game of Life rules
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    next_gen[i, j] = 0
                else:
                    next_gen[i, j] = 1
            else:
                if total == 3:
                    next_gen[i, j] = 1
                else:
                    next_gen[i, j] = 0

    return next_gen.tolist()

@csrf_exempt
def update_grid(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        current_grid = data.get('grid')
        next_gen = calculate_next_generation(current_grid)
        return JsonResponse({'grid': next_gen})
    
    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def new_grid(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        width = data.get('width', 50)
        height = data.get('height', 50)
        grid = initialize_grid(width, height)
        return JsonResponse({'grid': grid})
    
    return JsonResponse({'error': 'Invalid request method'})

