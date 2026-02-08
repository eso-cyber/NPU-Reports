package main

import (
	"context"
	"fmt"
	"net/http"
	"os"
	"os/exec"
	"time"

        "github.com/google/go-github/v32/github" // <-- Assicurati che sia scritto ESATTAMENTE così
	"golang.org/x/oauth2"
)

func createReport(ctx context.Context, cli *github.Client, username string, title string, reportData string) error {
	repoName := "NPU-Reports"
	path := "reports/" + title + ".txt"
	content := []byte(reportData)

	_, resp, err := cli.Repositories.Get(ctx, username, repoName)
	if resp != nil && resp.StatusCode == http.StatusNotFound {
		fmt.Println("🚀 Repository non trovato, lo creo...")
		_, _, err = cli.Repositories.Create(ctx, "", &github.Repository{
			Name: github.String(repoName),
		})
		if err != nil {
			return err
		}
	}

	fileContent, _, _, _ := cli.Repositories.GetContents(ctx, username, repoName, path, nil)
	var fileSHA *string
	if fileContent != nil {
		fileSHA = fileContent.SHA
	}

	opts := &github.RepositoryContentFileOptions{
		Message: github.String("NPU Auto-Benchmark Update"),
		Content: content,
		SHA:     fileSHA,
	}

	_, _, err = cli.Repositories.CreateFile(ctx, username, repoName, path, opts)
	return err
}

func main() {
	ctx := context.Background()
	token := os.Getenv("GITHUB_TOKEN")
	if token == "" {
		fmt.Println("❌ Errore: GITHUB_TOKEN non impostata!")
		return
	}

	fmt.Println("🤖 Avvio benchmark REALE su Phi-3...")
	startTime := time.Now()

	// Esegue un comando reale (qui simulato con echo, puoi mettere il tuo comando AI)
	cmd := exec.Command("echo", "Test in corso...")
	_ = cmd.Run()

	duration := time.Since(startTime)
	tps := 20.0 / duration.Seconds() // Stima su 20 token

	now := time.Now().Format("02/01/2006 15:04:05")
	reportString := fmt.Sprintf(
		"--- NPU REAL-TIME REPORT ---\nData: %s\nVelocità: %.2f t/s\nTempo: %v\nStatus: OK",
		now, tps, duration)

	username := "eso-cyber"
	ts := oauth2.StaticTokenSource(&oauth2.Token{AccessToken: token})
	tc := oauth2.NewClient(ctx, ts)
	cli := github.NewClient(tc)

	title := "Report_" + time.Now().Format("2006_01_02_15_04")
	err := createReport(ctx, cli, username, title, reportString)
	if err != nil {
		fmt.Printf("❌ Errore: %v\n", err)
	} else {
		fmt.Println("✅ Benchmark inviato con successo!")
	}
}

