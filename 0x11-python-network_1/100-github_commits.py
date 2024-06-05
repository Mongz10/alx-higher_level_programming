import requests
import sys

def fetch_repository_info(repository_name, owner_name):
    # Construct the URL for repository information
    repo_url = f"https://api.github.com/repos/{owner_name}/{repository_name}"

    try:
        # Send an HTTP GET request to fetch repository data
        repo_response = requests.get(repo_url)
        if repo_response.status_code == 200:
            repo_data = repo_response.json()
            print(f"Repository: {repo_data.get('name', 'N/A')}")
            print(f"Description: {repo_data.get('description', 'N/A')}")
            print(f"Stargazers Count: {repo_data.get('stargazers_count', 0)}")
        else:
            print(f"Error fetching repository data. Status code: {repo_response.status_code}")

        # Construct the URL for commits
        commits_url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"
        commits_response = requests.get(commits_url)
        if commits_response.status_code == 200:
            commits_list = commits_response.json()
            for i in range(min(10, len(commits_list))):
                sha = commits_list[i].get('sha')
                commit = commits_list[i].get('commit')
                author = commit.get('author')
                name = author.get('name')
                print(f"{i + 1}: {sha} ({name})")
        else:
            print(f"Error fetching commits data. Status code: {commits_response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    fetch_repository_info(repository_name, owner_name)

