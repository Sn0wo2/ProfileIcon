icons_string = (
    "py,pycharm,java,kotlin,cs,go,dart,js,ts,"
    "html,css,sass,react,vue,vite,svg,"
    "express,fastapi,spring,ktor,"
    "mysql,postgres,mongodb,sqlite,redis,"
    "docker,nginx,cloudflare,gcp,ubuntu,linux,windows,workers,"
    "git,github,githubactions,gradle,maven,idea,rider,vscode,visualstudio,vim,webstorm,"
    "replit,regex,postman,gmail,azul,md,bots,discord,twitter"
)

remaining = icons_string.split(",")
selected = []

while remaining:
    print("\nRemaining:")
    print("\n".join(remaining))
    choice = input("Select an icon (name, or Enter to finish): ").strip()
    if choice == "":
        break
    if choice in remaining:
        remaining.remove(choice)
        selected.append(choice)
        print(f"Chosen: {choice}")
    else:
        print(f"Not found: {choice}")

print("\nFinal Selection:")
print(",".join(selected))
print("\nRemaining:")
print(",".join(remaining))
