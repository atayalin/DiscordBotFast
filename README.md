# DiscordBotFast

An application which is used to send different messages to different discord channels via different accounts.

----------------------

## Makefile Documentation

To create virtual environment and add requirements,

```bash
make install
```

To run the application,

```bash
make run
```

If virtual environment is created, to add requirements and run the application,

```bash
make build
```

To remove virtual environment from application,

```bash
make uninstall
```

----------------------

## Yaml Configuration File Documentation

### Clients

You can add a client after "clients" tag.

```yaml
    - token: str
      channels: channel
```

### Channels

You can add a channel after "channels" tag.

```yaml
    - channel_id: str
      message: str
      period: int
```

----------------------

## Possible Paths
### Run app from scratch

```bash
make install
make run 
```
